from django.http import JsonResponse

# Create your views here.
from core.models import Person, Car


def matches(request):
    if request.method == "GET":
        current_user = Person.objects.filter(id=request.GET['user_id']).first()
        cars = Car.objects.filter(free=True)
        cars_by_owner = {}
        response = []
        for car in cars:
            if car.owner.id != current_user.id:
                if car.owner.id in cars_by_owner:
                    cars_by_owner[car.owner.id].append({
                        "id": car.id,
                        "seats": car.seats,
                        "animals": car.animals,
                        "brand": car.brand
                    })
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
