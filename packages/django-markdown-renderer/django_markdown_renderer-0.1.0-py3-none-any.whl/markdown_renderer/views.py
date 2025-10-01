from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.shortcuts import render
import json
import markdown2
import bleach

ALLOWED_TAGS = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
                'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
                'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'hr', 'br']

ALLOWED_ATTRIBUTES = {
    'a': ['href', 'title', 'alt', 'rel', 'target', 'dir'],
    '*': ['id', 'class']
}

class IndexView(TemplateView):
    template_name = 'markdown_renderer/index.html'

@csrf_exempt
def render_markdown(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
        
    try:
        data = json.loads(request.body)
        markdown = str(data.get('markdown', ''))
        
        if not markdown:
            return JsonResponse({'error': 'markdown is required'}, status=400)
            
        if len(markdown) > 200_000:
            return JsonResponse({'error': 'markdown too large'}, status=413)

        # Convert Markdown to HTML
        html = markdown2.markdown(markdown, extras=['fenced-code-blocks', 'tables'])
        
        # Clean HTML
        clean_html = bleach.clean(html,
                                tags=ALLOWED_TAGS,
                                attributes=ALLOWED_ATTRIBUTES,
                                strip=True)

        return JsonResponse({'html': clean_html})
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return JsonResponse({'error': 'render failed'}, status=500)

def health_check(request):
    return JsonResponse({'ok': True})
