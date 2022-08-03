from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify
from .models import Tool
from .forms import CommentForm, ToolForm



class ToolList(generic.ListView):
    model = Tool
    queryset = Tool.objects.filter(published_status=1).order_by('-date_added')
    template_name = 'tools.html'
    paginate_by = 6


'''Displays detailed view of individual tool card'''


class ToolDetail(View):
    def get(self, request, slug, *args, **kwargs):
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
        queryset = Tool.objects.filter(published_status=1)
        tool = get_object_or_404(queryset, slug=slug)
        comments = tool.comments.filter(approved=True).order_by('date_added')
        liked = False
        if tool.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        '''Get the data posted from the form and assign to variable'''
        comment_form = CommentForm(data=request.POST)

        '''
        If all fields completed, forms is valid and 
        a comment had been left to be processed
        '''
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            '''Assign a tool to the form before commiting to database'''
            comment = comment_form.save(commit=False)
            comment.tool = tool
            comment.save()
        else:
            '''Return an empty form instance if form not completed'''
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


'''Tool likes'''


class ToolLike(View):

    def post(self, request, slug):
        tool = get_object_or_404(Tool, slug=slug)

        if tool.likes.filter(id=request.user.id).exists():
            tool.likes.remove(request.user)
        else:
            tool.likes.add(request.user)      
        '''Reload tool detail template to see the likes status'''
        return HttpResponseRedirect(reverse('tool_detail', args=[slug]))


'''Renders a home page template'''


class HomePageView(generic.TemplateView):
    template_name = 'index.html'


'''Renders tools added by the logged in user'''


class MyToolsView(LoginRequiredMixin, generic.ListView):
    template_name = 'my_tools.html'
    paginate_by = 6
   
    def get_queryset(self):
        return Tool.objects.filter(author_name=self.request.user)


class AddTool(LoginRequiredMixin, View):

    def get(self, request):
        tool_form = ToolForm()
        context = {'tool_form': tool_form }

        return render(
            request,
            'add_tool.html', context
        )
    
    def post(self, request):
        '''Get the data posted from the form and assign to variable'''
        tool_form = ToolForm(request.POST, request.FILES)

        if tool_form.is_valid():
            tool = tool_form.save(commit=False)
            tool_form.instance.author_name = request.user
            tool.slug = slugify(tool.tool_name)
            messages.success(request, 'Your post has been submitted!')
            tool.save()
            return redirect('mytools')
        
        else:
            tool_form = ToolForm()
        
        return render(
            request, 'add_tool.html', {'tool_form': tool_form}
            )


class EditTool(LoginRequiredMixin, View):
    '''View for editing and updating an existing tool'''

    def get(self, request, tool_id):
        tool = get_object_or_404(Tool, id=tool_id)

        return render(
            request,
            'edit_tool.html', 
            {
                'tool_form': ToolForm(instance=tool)
            }
        )
    
    def post(self, request, tool_id):
        '''Get the tool_id passed in via URL, submit form data and redirect'''
        tool = get_object_or_404(Tool, id=tool_id)
        tool_form = ToolForm(data=request.POST, instance=tool)

        if tool_form.is_valid():
            tool.save()            
            messages.success(request, 'Your edited post has been submitted!')
            
            return redirect('mytools')
        
        else:
            return render(
            request, 'edit_tool.html', {'tool_form': tool_form}
            )
