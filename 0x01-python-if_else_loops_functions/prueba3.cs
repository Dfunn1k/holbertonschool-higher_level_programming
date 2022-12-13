using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace program
{
	class program
	{
		static void Main()
		{
			int rendimiento = 0;
			int años = 0;
			int mensualidad = 850;
			int descuento = 0;

			console.writeLine("Seleccione el rendimiento acádemico");
			console.writeLine("1. 1er y 2do puesto");
			console.writeLine("2. décimo superior");
			console.writeLine("3. quinto superior");
			console.writeLine("4. tercio superior");
			console.writeLine("5. Regular");
			rendimiento = int.Parse(console.ReadLine());
			console.writeLine("Cuantos años lleva estudiando");
			años = int.Parse(console.ReadLine());

			switch(rendimiento)
			{
				case 1: if(años >= 1)
					{
						console.writeLine("Usted ha sido becado!");
					}
					else
					{
						console.writeLine("No cumple el tiempo minimo para recibir la beca");
					}
				case 2: if (años >= 1)
					{
						descuento = mensualidad * 0.8;
						mensualidad -= descuento;
						console.writeLine("La mensualidad ahora es: " + mensualidad);
					}
			
				case 3: if (años >= 1)
					{
						descuento = mensualidad * 0.6;
						mensualidad -= descuento;
						console.writeLine("La mensualidad ahora es: " + mensualidad);
					}

				case 4: if (años >= 1)
					{
						descuento = mensualidad * 0.3;
						mensualidad -= descuento;
						console.writeLine("La mensualidad ahora es: " + mensualidad);
					}
				case 5:
				{
					Console.WriteLine("La mensualidad es: " + mensualidad);
				}
			}
		}
	}
}