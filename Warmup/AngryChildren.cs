using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HackerRank.Warmup
{
    class AngryChildren
    {
        static void Main(string[] args)
        {
            int n = Convert.ToInt32(Console.ReadLine());
            int k = Convert.ToInt32(Console.ReadLine());
            List<long> candies = new List<long>();
            long diff = 0;

            for (int i = 0; i < n; i++)
            {
                candies.Add(Convert.ToInt64(Console.ReadLine()));
            }

            candies.Sort();

            long min = 0;

            for (int i = 0; i < (n - k); i++)
            {
                diff = candies[i + k - 1] - candies[i];

                if (i == 0)
                {
                    min = diff;
                }
                else if (min > diff)
                {
                    min = diff;
                }
            }

            Console.WriteLine(min);

            Console.ReadLine();
        }
    }
}
