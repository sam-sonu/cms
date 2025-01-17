
def admin_context(request):
    context = {}
    
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Check if the user is a superuser (admin)
        if request.user.is_superuser:
            context['is_admin'] = True
            context['current_user'] = request.user
        else:
            context['is_admin'] = False
            context['current_user'] = request.user
    else:
        context['is_admin'] = False
        context['current_user'] = None
    
    return context