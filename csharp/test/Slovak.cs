using NUnit.Framework;

using System;

using word2number;

namespace test.word2number
{

    public class Slovak
    {
        
        [SetUp]
        public void SetUp () {	
            Environment.SetEnvironmentVariable ("w2n.lang","sk");
        }

        [Test]
        public void Test_Positives () {
            Assert.AreEqual(new W2N().wordToNum("devätnásť"), 19);
            Assert.AreEqual(new W2N().wordToNum("sto"), 100);
            Assert.AreEqual(new W2N().wordToNum("tisíc"), 1000);
            Assert.AreEqual(new W2N().wordToNum("tisíc jedna"), 1001);
            Assert.AreEqual(new W2N().wordToNum("tisíc jeden"), 1001);
        }
    }
}
