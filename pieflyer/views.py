from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import Context, loader
from .models import Score

# Create your views here.
def game(request):
    template = loader.get_template("pieflyer/gamedoc.html")
    
    highest_score_list = Score.objects.order_by('-score')[:5]
    if len(highest_score_list) is 6:
        recycled_score = Score.objects.values_list()[5]
    context = {'highest_score_list': highest_score_list, 'recycled_score': recycled_score}
    
    
    return render(request, 'pieflyer/gamedoc.html', context)

def index(request):
    highest_score_list = Score.objects.order_by('-score')[:5]
    context = {'highest_score_list': highest_score_list}
    
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))