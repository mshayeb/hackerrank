using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HackerRank.Warmup
{
    // This solution fails some test cases with time limit exceeded
    class SherlockandQueries
    {
        static void Main(string[] args)
        {
            byte[] bytes = new byte[2000];
            Stream inputStream = Console.OpenStandardInput(bytes.Length);
            Console.SetIn(new StreamReader(inputStream));

            long[] nm = Console.ReadLine().Split(' ').Select(x => long.Parse(x)).ToArray();
            long n = nm[0];
            long m = nm[1];

            long[] a = Console.ReadLine().Split(' ').Select(x => long.Parse(x)).ToArray();
            long[] b = Console.ReadLine().Split(' ').Select(x => long.Parse(x)).ToArray();
            long[] c = Console.ReadLine().Split(' ').Select(x => long.Parse(x)).ToArray();

            Dictionary<long, long[]> biOccur = new Dictionary<long, long[]>();
            long[] occurences = new long[n];

            for (long i = 0; i < m; i++)
            {
                for(long j = 0; j < n; j++)
                {
                    occurences[j] = (long)((j + 1) / b[i]);
                }

                biOccur.Add(b[i], occurences);
            }

            for (long i = 0; i < m; i++)
            {
                long t = b[i];

                while (t <= n)
                {
                    a[t - 1] = (a[t - 1] * c[i]) % 1000000007;
                    t = t + b[i];
                }
            }

            string prefix = "";
            for (long i = 0; i < n; i++)
            {
                Console.Write(prefix);
                Console.Write(a[i]);
                prefix = " ";
            }

            Console.WriteLine();
            Console.ReadLine();
        }
    }
}