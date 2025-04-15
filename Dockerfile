#Użycie lekkiego obrazu Pythona
FROM python:3.9-slim

#Ustawienie katalogu roboczego
WORKDIR /app

#Kopiowanie plików aplikacji
COPY . /app

#Instalacja zależności
RUN pip install --no-cache-dir -r requirements.txt

#Wystawienie portu
EXPOSE 5000

#Uruchomienie serwera Gunicorn
CMD ["python", "app.py"]
