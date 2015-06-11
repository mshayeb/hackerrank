using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HackerRank.Warmup
{
    class HalloweenParty
    {
        static void Main(string[] args)
        {
            int testCases = Convert.ToInt32(Console.ReadLine());
            List<long> kList = new List<long>();
            long m = 0;
            long n = 0;

            for (int i = 0; i < testCases; i++)
            {
                kList.Add(Convert.ToInt64(Console.ReadLine()));
            }

            foreach (long k in kList)
            {
                m = k / 2;
                n = k - m;

                Console.WriteLine(m * n);
            }

            Console.ReadLine();
        }
    }
}
