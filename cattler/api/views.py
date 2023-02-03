import random
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from .models import Lot, Corral, Troop, Animal
from .serializers import LotSerializer, CorralSerializer, TroopSerializer, AnimalSerializer
from django.db import transaction


class AnimalCreate(generics.CreateAPIView):
    # Crea animales
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    

class TroopCreate(generics.CreateAPIView):
    # Crea tropas
    queryset = Troop.objects.all()
    serializer_class = TroopSerializer
            
class CorralCreate(generics.ListCreateAPIView):
    # Crea corrales y los consulta
    queryset = Corral.objects.all()
    serializer_class = CorralSerializer


class LotCreate(generics.ListCreateAPIView):
    # Crea lotes y los consulta
    queryset = Lot.objects.all()
    serializer_class = LotSerializer


class getAnimals(APIView):
    # Consulta animales (permite filtrar por tropa)
    def get(self, request, format=None):
        try:
            troop = request.data.get('troop')
            if troop:
                if isinstance(troop,int):
                    animals = Animal.objects.filter(troop__troop_number=troop)
                    if not animals:
                        return Response({'error': 'No se encontró animales en la tropa especificada'}, status=404)
                    serializable_animals = AnimalSerializer(animals, many=True)
                    return Response({'data': serializable_animals.data}, status=200) 
                else:
                    return Response({'error': 'El numero de tropa es erroneo'}, status=404)
            
            animals = Animal.objects.all()
            serializable_animals = AnimalSerializer(animals, many=True)
            return Response({'data': serializable_animals.data}, status=200)     
        except:
             return Response({'error': 'Se ha producido un error'}, status=404)
         
class getTroops(APIView):
    # Consulta tropas (permite filtrar por lote)
    def get(self, request, format=None):
        try:
            lot = request.data.get('lot')
            if lot:
                if isinstance(lot,int):
                    troops = Troop.objects.filter(lot__lot_number=lot)
                    if not troops:
                        return Response({'error': 'No se encontraron tropas en el lote especificado'}, status=404)
                    serializable_troops = TroopSerializer(troops, many=True)
                    return Response({'data': serializable_troops.data}, status=200) 
                else:
                    return Response({'error': 'El numero de tropa es erroneo'}, status=404)
            
            troops = Troop.objects.all()
            serializable_troops = TroopSerializer(troops, many=True)
            return Response({'data': serializable_troops.data}, status=200)     
        except:
             return Response({'error': 'Se ha producido un error'}, status=404)
    

class AnimalIngressView(APIView):
    # Permite ingresar animales en el formato indicado - Chequeo de transaccion atomica
    def post(self, request, format=None):
        try:
            with transaction.atomic():
                lot = request.data.get('lote')
                ingresses = request.data.get('ingresos')
                if isinstance(lot,int) and isinstance(ingresses, list):
                    try:
                        lot = Lot.objects.get(lot_number=lot)
                    except Lot.DoesNotExist:
                        return Response({'error': 'No se encontro el lote especificado'}, status=404)
                    for ingress in ingresses:
                        corral_num = ingress.get('corral')
                        quantity = ingress.get('cantidad')
                        troop_num = random.randint(1,100) # Ya que no se especifica que hacer con el numero de tropa se lo asigna de manera random
                        if isinstance(corral_num,int) and isinstance(quantity,int):
                            try:
                                corral = Corral.objects.get(corral_number=corral_num)
                            except Corral.DoesNotExist:
                                return Response({'error': 'No se encontró el corral especificado'}, status=404)
                            
                            troop_exists = Troop.objects.filter(troop_number=troop_num, lot=lot).exists()
                            if troop_exists:
                                return Response({'error': 'Ya hay una tropa con ese numero en ese lote'}, status=404)
                            if corral.troop is None:
                                troop = Troop.objects.create(
                                    troop_number=troop_num,
                                    lot=lot
                                )
                                for i in range(quantity):
                                    Animal.objects.create(
                                        troop=troop,
                                    )
                                Corral.objects.filter(corral_number=corral_num).update(troop=troop)
                            else:
                                return Response({'error': 'El corral ya tiene animales ingresados'}, status=404)
                        else:
                            return Response({'error': 'Corral o cantidad erroneos'}, status=404)

                    return Response({'message': 'Los animales se han ingresado con éxito'}, status=200) 
                else:
                    return Response({'error': 'No se proporcionaron todos los datos necesarios para el ingreso de animales'}, status=404)
        except:
            return Response({'error': 'Se ha producido un error'}, status=404)