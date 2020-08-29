from django.http import HttpResponseRedirect
from django.views.generic import ListView
from product import models as prd
from substitute import models as sub
from django.urls import reverse
from django.contrib.auth.decorators import login_required

PAGINATE_BY_NB = 10

#@login_required
class ListRegisteredSubstitutes(ListView):
    template_name = "substitute/registered_substitutes.html"  # chemin vers les subtituts
    model = sub.Substitute
    context_object_name = "substituts_enregistres"
    paginate_by = PAGINATE_BY_NB

    def get_queryset(self):
        current_user = self.request.user
        if current_user is not None:
            return sub.Substitute.objects.filter(user_subst = current_user)


@login_required
def delete_substituts(request):
    idProduct = request.GET.get("origin")
    idSubstitute = request.GET.get("sub")
    p_origin = prd.Product.objects.get(pk=idProduct)
    p_substitute = prd.Product.objects.get(pk=idSubstitute)

    sub.Substitute.objects.filter (
        user_subst = request.user,
        product_origin = p_origin,
        product_substitute = p_substitute
        ).delete()

    # check if it is the last row on the last page
    value_page = request.GET.get("page")
    current_page = int("1" if value_page is None else value_page)
    last_on_last_page = (sub.Substitute.objects.count() % PAGINATE_BY_NB) == 0 \
                        and (sub.Substitute.objects.count() // PAGINATE_BY_NB) + 1 == current_page

    if current_page is not None and current_page > 1:
        if last_on_last_page is True:
            if not request.GET._mutable:
                request.GET._mutable = True
            request.GET["page"] = str(current_page - 1)

    reverse_url = reverse('substitutes_list')

    add_params = '&'.join([key + '=' + param
                           for key, param
                           in request.GET.items()
                           if key not in ['origin', 'sub']])
    if add_params is not None:
        reverse_url = reverse_url + '?' + add_params

    return HttpResponseRedirect(reverse_url)