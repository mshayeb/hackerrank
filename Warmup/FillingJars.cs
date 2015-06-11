using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HackerRank.Warmup
{
    class FillingJars
    {
        static void Main(string[] args)
        {
            long[] nm = Console.ReadLine().Split(' ').Select(x => long.Parse(x)).ToArray();
            long n = nm[0];
            long m = nm[1];
            long[] abk;
            long a = 0;
            long b = 0;
            long k = 0;
            long sum = 0;

            for (long i = 0; i < m; i++)
            {
                abk = Console.ReadLine().Split(' ').Select(x => long.Parse(x)).ToArray();
                a = abk[0];
                b = abk[1];
                k = abk[2];

                sum = sum + (b - a + 1) * k;
            }

            Console.WriteLine((long)Math.Floor((double)sum / n));

            Console.ReadLine();
        }
    }
}
