def add_view_to_car(today, view_satistic):
    if str(today.year) in view_satistic:
        new_view = view_satistic[str(today.year)]
    else:
        new_view = {}

    if today.strftime('%Y-%m-%d') in new_view:
        new_view[today.strftime('%Y-%m-%d')] += 1
    else:
        new_view[today.strftime('%Y-%m-%d')] = 1

    view_satistic[str(today.year)]= new_view
    return view_satistic
