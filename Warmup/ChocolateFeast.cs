using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HackerRank.Warmup
{
    class ChocolateFeast
    {
        static void Main(string[] args)
        {
            int testCases = Convert.ToInt32(Console.ReadLine());
            List<string> ncmList = new List<string>();
            int n = 0;
            int c = 0;
            int m = 0;
            int chocolatesBought = 0;
            int wrappers = 0;

            for (int i = 0; i < testCases; i++)
            {
                ncmList.Add(Console.ReadLine());
            }

            foreach (string ncm in ncmList)
            {
                string[] ncmSplit = ncm.Split(' ');
                n = Convert.ToInt32(ncmSplit[0]);
                c = Convert.ToInt32(ncmSplit[1]);
                m = Convert.ToInt32(ncmSplit[2]);

                double choc = n / c;
                chocolatesBought = (int)Math.Floor(choc);
                wrappers = chocolatesBought;

                while (wrappers >= m)
                {
                    chocolatesBought = chocolatesBought + 1;
                    wrappers = wrappers + 1;
                    wrappers = wrappers - m;
                }

                Console.WriteLine(chocolatesBought);
            }

            Console.ReadLine();
        }
    }
}
