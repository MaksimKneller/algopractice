// See https://aka.ms/new-console-template for more information
using Sorting;
using System.Diagnostics;
using System.Linq;

Console.WriteLine("Starting...");

/* GENERATE SAMPLE DATA */
List<Employee> employees = new();

for (int i = 1; i <= 10; i++) employees.Add(new Employee() { Id=i, Salary=i*10000});
employees = employees.OrderBy(e => Guid.NewGuid()).ToList();


/* SELECTION SORT */
Selection<Employee> SelSort = new(employees);
List<Employee> result = SelSort.Sort();

Console.WriteLine(string.Format("Result: {0}", string.Join(",",employees.Select(e => e.Salary))));




