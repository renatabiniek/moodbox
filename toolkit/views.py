from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Tool
from django.contrib.auth.models import User
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin


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

