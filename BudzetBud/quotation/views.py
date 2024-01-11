from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from BudzetBud.quotation.forms import CreateHalfStageForm
from BudzetBud.quotation.models import UnderStage


@login_required
def makeView(request):

    ustage = UnderStage.all()
    formustage = CreateHalfStageForm(request.POST)
    userid = request.user.id
    return render(request,
                  'quotation/create.html',
                  {'formustage':formustage}
                  )
