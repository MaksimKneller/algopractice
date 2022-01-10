using System;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sorting
{
    internal class Selection<T> where T : IComparable<T>
    {
        private List<T> data = new();
        public Selection(List<T> _data)
        {
            Console.WriteLine(string.Format("Selection Sort: {0} elements", _data.Count));
            data = _data;
        }

        public List<T> Sort()
        {
            for (int x=0; x<data.Count-1; x++)
            {
                int minIndx = x;

                for (int y=x+1; y<data.Count; y++)
                {
                    //Console.WriteLine(string.Format("Comparing {0},{1}", data[minIndx], data[y]));
                    if (data[minIndx].CompareTo(data[y]) > 0) minIndx = y;                   
                }

                //Console.WriteLine(string.Format("Swapping {0},{1}", data[x], data[minIndx]));
                (data[x],data[minIndx]) = (data[minIndx],data[x]);
                //Console.WriteLine(string.Format("Result: {0}", string.Join(",", data)));
            }

            return data;
        }


    }
}
