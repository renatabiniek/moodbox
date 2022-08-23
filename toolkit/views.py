"""Views"""
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect, Http404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify
from .models import Tool, Category
from .forms import CommentForm, ToolForm


class ToolList(LoginRequiredMixin, generic.ListView):
    """View to display list of published tools added
    by users, ordered by date in descending order and paginated.
    If user not logged in, they're redirected to login page via
    LoginRequiredMixin.
    """
    model = Tool
    queryset = Tool.objects.filter(published_status=1).order_by('-date_added')
    template_name = 'tools.html'
    paginate_by = 6

    # Code from Codemy.com tutorial 'How to add blog category navbar links"

    def get_context_data(self, *args, **kwargs):
        """Get all category names."""
        cat_menu = Category.objects.all()
        context = super(ToolList, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class ToolDetail(LoginRequiredMixin, View):
    """View to display details of individual tool card."""

    def get(self, request, slug, *args, **kwargs):
        """Display all published tools, their comments and likes."""
        queryset = Tool.objects.filter(published_status=1)
        tool = get_object_or_404(queryset, slug=slug)
        comments = tool.comments.filter(approved=True).order_by('date_added')
        liked = False
        if tool.likes.filter(id=self.request.user.id).exists():
            liked = True
        return render(
            request,
            'tool_detail.html',
            {
                'tool': tool,
                'comments': comments,
                'commented': False,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """Submit form content to database."""
        queryset = Tool.objects.filter(published_status=1)
        tool = get_object_or_404(queryset, slug=slug)
        comments = tool.comments.filter(approved=True).order_by('date_added')
        liked = False
        if tool.likes.filter(id=self.request.user.id).exists():
            liked = True

        # Get the data posted from the form and assign to variable.
        comment_form = CommentForm(data=request.POST)

        # If all fields completed, forms is valid
        # and a comment had been left to process.

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            # Assign a tool to the form before committing to database.
            comment = comment_form.save(commit=False)
            comment.tool = tool
            comment.save()
        else:
            # Return an empty form instance if form not completed.
            comment_form = CommentForm()

        return render(
            request,
            'tool_detail.html',
            {
                'tool': tool,
                'comments': comments,
                'commented': True,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )


class ToolLike(View):
    """Tool likes"""

    def post(self, request, slug):
        """Submit like/unlike."""
        tool = get_object_or_404(Tool, slug=slug)

        if tool.likes.filter(id=request.user.id).exists():
            tool.likes.remove(request.user)
        else:
            tool.likes.add(request.user)
        # Reload tool detail template to see the likes status
        return HttpResponseRedirect(reverse('tool_detail', args=[slug]))


class HomePageView(generic.TemplateView):
    """Render a home page template."""
    template_name = 'index.html'

    # Code from Codemy.com tutorial 'How to add blog category navbar links"
    def get_context_data(self, *args, **kwargs):
        """Get all category names."""
        cat_menu = Category.objects.all()
        context = super(HomePageView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class MyToolsView(LoginRequiredMixin, generic.ListView):
    """Render tools added by the logged in user."""
    template_name = 'my_tools.html'
    paginate_by = 6

    def get_queryset(self):
        return Tool.objects.filter(author_name=self.request.user)


class AddTool(LoginRequiredMixin, View):
    """Add Tool view that handles the form to add new tool."""
    def get(self, request):
        """Display the form to add new tool."""
        tool_form = ToolForm()
        context = {'tool_form': tool_form}

        return render(
            request,
            'add_tool.html', context
        )

    def post(self, request):
        """
        Get the form data, redirect to my tools page if valid,
        or display the form again if not.
        """
        tool_form = ToolForm(request.POST, request.FILES)

        if tool_form.is_valid():
            tool = tool_form.save(commit=False)
            tool_form.instance.author_name = request.user
            tool.slug = slugify(tool.tool_name)
            messages.success(request, 'Your post has been submitted!')
            tool.save()
            return redirect('mytools')

        else:
            print('form invalid')

        return render(
            request, 'add_tool.html', {'tool_form': tool_form}
        )


class EditTool(LoginRequiredMixin, View):
    """View for editing and updating an existing tool."""

    def get(self, request, tool_id):
        """Get the tool id passed in via URL, check if the user is the author
        of the tool, return tool form with prepopulated original data,
        or raise HTTP404 error is the user is not the author.
        """
        tool = get_object_or_404(Tool, id=tool_id)

        if request.user == tool.author_name:

            return render(
                request,
                'edit_tool.html',
                {
                    'tool_form': ToolForm(instance=tool)
                }
            )
        else:
            raise Http404("Only author can edit this tool")

    def post(self, request, tool_id):
        """Get the tool id passed in via URL, submit form data and redirect."""
        tool = get_object_or_404(Tool, id=tool_id)
        tool_form = ToolForm(request.POST, request.FILES, instance=tool)

        if tool_form.is_valid():
            # After editing a tool, tool needs to be approved again
            # before it gets published.
            tool = tool_form.save(commit=False)
            if tool.published_status == 1:
                tool.published_status = 0
            tool.save()
            messages.success(request, 'Your edited post has been submitted!')

            return redirect('mytools')

        else:
            return render(
                request, 'edit_tool.html', {'tool_form': tool_form}
            )


class DeleteTool(LoginRequiredMixin, View):
    """View for deleting an existing tool."""

    def get(self, request, tool_id):
        """Get request and redirect to 404 page."""
        raise Http404('This page doesnt exist')

    def post(self, request, tool_id):
        """
        Delete tool if allowed for the user
        and redirect to my tools page.
        """
        tool = get_object_or_404(Tool, id=tool_id)
        if request.user == tool.author_name:
            tool.delete()
            messages.success(request, 'Your tool has been deleted')
            return redirect('mytools')
        else:
            raise Http404('You cannot delete this')


def category_view(request, slug):
    """ Displays tools related to the category
    passed through the category slug.
    """
    cats = get_object_or_404(Category, slug=slug)
    
    all_categories = cats.categories.all

    context = {
        'cats': cats,
        'all_categories': all_categories
    }

    return render(request, 'categories.html', context)
