using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HackerRank.Warmup
{
    class GemStones
    {
        static void Main(string[] args)
        {
            int rocks = Convert.ToInt32(Console.ReadLine());
            Dictionary<char, int> elementCount = new Dictionary<char, int>();
            List<string> rockCompositionList = new List<string>();
            string rockComposition;
            int gemElementCount = 0;

            for (int i = 0; i < rocks; i++)
            {
                rockComposition = Console.ReadLine();
                rockCompositionList.Add(rockComposition);
            }

            for (int c = 97; c <= 122; c++)
            {
                foreach (string rc in rockCompositionList)
                {
                    if (rc.Contains((char)c))
                    {
                        if (elementCount.ContainsKey((char)c))
                        {
                            elementCount[(char)c] = elementCount[(char)c] + 1;
                        }
                        else
                        {
                            elementCount.Add((char)c, 1);
                        }
                    }
                    else
                    {
                        break;
                    }
                }
            }

            for (int c = 97; c <= 122; c++)
            {
                if (elementCount.ContainsKey((char)c))
                {
                    if (elementCount[(char)c] == rocks)
                    {
                        gemElementCount++;
                    }
                }
            }

            Console.WriteLine(gemElementCount);
            Console.ReadLine();
        }
    }
}
