using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sorting
{
    internal struct Employee : IComparable<Employee>
    {
        public int Id;
        public double Salary;

        public int CompareTo(Employee other)
        {
            return Salary.CompareTo(other.Salary);
        }
    }
}
