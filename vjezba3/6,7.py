'''
Zad6
Kada pozovemo task2 = asyncio.create_task(fetch_data(2)), korutina fetch_data(2) se registrira u event loop i dobiva stanje SCHEDULED. 
Makar je u main() nikada ne awaitamo, event loop će ju svejedno izvršiti u pozadini, jer je create_task() samostalno pokreće.
Dok main() čeka await task1, event loop nastavlja izvršavati sve ostale zakazane taskove, uključujući i task2. 
Zato se ispis „Dovršio sam s 2.“ pojavljuje bez potrebe da eksplicitno awaitamo task2.

Zad7
asyncio.run(main()) pokreće event loop i unutar main() se kreiraju tri taska pomoću asyncio.create_task().
Svi taskovi odmah dobivaju stanje SCHEDULED i počnu se izvršavati.
Svaki timer ispiše preostale sekunde i zatim ode na await asyncio.sleep(1), čime prelazi u stanje SUSPENDED.
Nakon svake sekunde event loop probudi sve timere i oni nastavljaju odbrojavanje.
Timer 1 završava nakon 3 sekunde, Timer 2 nakon 5, a Timer 3 nakon 7 sekundi (stanje FINISHED).
asyncio.gather() čeka da svi taskovi završe, a zatim main() završava i event loop se zatvara.
'''