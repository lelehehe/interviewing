using System;
using NUnit.Framework;

namespace MyLib
{
    public class Sample1
    {
        public static int AddInts(int x, int y)
        {
            return x + y;
        }
    }

    [TestFixture]
    class Sample1Tests
    {
        [TestCase(2, 4, 5)]
        [TestCase(1, 0, 1)]
        [TestCase(10, -2, 8)]
        public void Should_Return_Sum_Given_Ints(int x, int y, int z)
        {
            var result = Sample1.AddInts(x, y);
            Assert.AreEqual(z, result);
        }
    }    
}
