from django.http import JsonResponse

from core.models import Person, Car


def matches(request):
    if request.method == "GET":
        try:
            current_user = Person.objects.filter(id=request.GET['user_id']).first()
        except KeyError:
            return JsonResponse({"success": "failure"}, status=400)
        try:
            filter_min_age = int(request.GET['min_age'])
        except KeyError:
            filter_min_age = 0
        try:
            filter_max_age = int(request.GET['max_age'])
        except KeyError:
            filter_max_age = 2147483647
        try:
            if request.GET['animals'] == "true":
                filter_animals = True
            else:
                filter_animals = False
        except KeyError:
            filter_animals = False
        cars = Car.objects.filter(free=True)
        cars_by_owner = {}
        response = []
        for car in cars:
            if car.owner.id != current_user.id and filter_min_age <= car.owner.age <= filter_max_age:
                if car.owner.id in cars_by_owner:
                    if filter_animals:
                        if car.animals:
                            cars_by_owner[car.owner.id].append({
                                "id": car.id,
                                "seats": car.seats,
                                "animals": car.animals,
                                "brand": car.brand
                            })
                    else:
                        cars_by_owner[car.owner.id].append({
                            "id": car.id,
                            "seats": car.seats,
                            "animals": car.animals,
                            "brand": car.brand
                        })
                else:
                    if filter_animals:
                        if car.animals:
                            cars_by_owner[car.owner.id] = ([{
                                "id": car.id,
                                "seats": car.seats,
                                "animals": car.animals,
                                "brand": car.brand
                            }])
                    else:
                        cars_by_owner[car.owner.id] = ([{
                            "id": car.id,
                            "seats": car.seats,
                            "animals": car.animals,
                            "brand": car.brand
                        }])

    for car_owner_id, cars_by_owner_value in cars_by_owner.items():
        car_owner = Person.objects.filter(id=car_owner_id).first()
        response.append({
            "id": car_owner.id,
            "age": car_owner.age,
            "name": car_owner.name,
            "email": car_owner.email,
            "interests": car_owner.interests,
            "cars": cars_by_owner_value
        })

    return JsonResponse(response, safe=False)
