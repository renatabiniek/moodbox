from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Tool
from .forms import CommentForm


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
                'liked': liked,
                'comment_form': CommentForm(),
            },
        )


'''Renders a home page template'''


class HomePageView(generic.TemplateView):
    template_name = 'index.html'
