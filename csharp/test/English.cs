using NUnit.Framework;

using System;

using word2number;

namespace vampire.test.dotnet
{

    /// <summary>
    /// This test throws compiler error if not supported.
    /// So last call is Assert.True(true);
    /// </summary>
    public class English
    {
        
        [SetUp]
        public void SetUp () {	
            Environment.SetEnvironmentVariable ("w2n.lang","en");
        }

        [Test]
        public void Test_Positives () {
            Assert.AreEqual(new W2N().wordToNum("two million three thousand nine hundred and eighty four"), 2003984);
            Assert.AreEqual(new W2N().wordToNum("nineteen"), 19);
            Assert.AreEqual(new W2N().wordToNum("two thousand and nineteen"), 2019);
            Assert.AreEqual(new W2N().wordToNum("two million three thousand and nineteen"), 2003019);
            Assert.AreEqual(new W2N().wordToNum("three billion"), 3000000000L);
            Assert.AreEqual(new W2N().wordToNum("three million"), 3000000);
            Assert.AreEqual(new W2N().wordToNum("one hundred twenty three million four hundred fifty six thousand seven hundred and eighty nine"), 123456789);
            Assert.AreEqual(new W2N().wordToNum("eleven"), 11);
            Assert.AreEqual(new W2N().wordToNum("nineteen billion and nineteen"), 19000000019L);
            Assert.AreEqual(new W2N().wordToNum("one hundred and forty two"), 142);
            Assert.AreEqual(new W2N().wordToNum("112"), 112);
            Assert.AreEqual(new W2N().wordToNum("11211234"), 11211234);
            Assert.AreEqual(new W2N().wordToNum("five"), 5);
            Assert.AreEqual(new W2N().wordToNum("two million twenty three thousand and forty nine"), 2023049);
            Assert.AreEqual(new W2N().wordToNum("two point three"), 2.3);
            Assert.AreEqual(new W2N().wordToNum("two million twenty three thousand and forty nine point two three six nine"), 2023049.2369);
            Assert.AreEqual(new W2N().wordToNum("one billion two million twenty three thousand and forty nine point two three six nine"), 1002023049.2369);
            Assert.AreEqual(new W2N().wordToNum("point one"), 0.1D);
            Assert.AreEqual(new W2N().wordToNum("point"), 0);
            Assert.AreEqual(new W2N().wordToNum("point nineteen"), 0);
            Assert.AreEqual(new W2N().wordToNum("one hundred thirty-five"), 135);
            Assert.AreEqual(new W2N().wordToNum("hundred"), 100);
            Assert.AreEqual(new W2N().wordToNum("thousand"), 1000);
            Assert.AreEqual(new W2N().wordToNum("million"), 1000000);
            Assert.AreEqual(new W2N().wordToNum("billion"), 1000000000);
            Assert.AreEqual(new W2N().wordToNum("one million and thousand"), 1_001_000);
            Assert.AreEqual(new W2N().wordToNum("nine point nine nine nine"), 9.999);
            Assert.AreEqual(new W2N().wordToNum("seventh point nineteen"), 0);
            Assert.AreEqual(new W2N().wordToNum("seven million, eight hundred, and sixty three thousand, two hundred, and fifty four"), 7863254);

            // test cases https://github.com/akshaynagpal/w2n/issues/54
            Assert.AreEqual(new W2N().wordToNum("three point nine seven"), 3.97);
            Assert.AreEqual(new W2N().wordToNum("two point seven eight"), 2.78);
            Assert.AreEqual(new W2N().wordToNum("one point eight six"), 1.86);
            Assert.AreEqual(new W2N().wordToNum("two point seven two"), 2.72);
            Assert.AreEqual(new W2N().wordToNum("one point eight four"), 1.84);
            Assert.AreEqual(new W2N().wordToNum("two point two eight"), 2.28);
            Assert.AreEqual(new W2N().wordToNum("two point four seven"), 2.47);
            Assert.AreEqual(new W2N().wordToNum("one point five nine"), 1.59);
            
            // test for kylosnite repository
            Assert.AreEqual(new W2N().wordToNum("nine million nine thousand"), 9009000);

            // in different to w2n it is ok, in result of str:112 is not different to int:112
            Assert.AreEqual(new W2N().wordToNum("112"), 112);
            Assert.AreEqual(new W2N().wordToNum(112),112);        
        }
    }
}
