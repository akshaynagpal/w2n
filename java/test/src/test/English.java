/**
 * SPDX-FileCopyrightText: 2020-2021 - Sebastian Ritter <bastie@users.noreply.github.com>
 * SPDX-License-Identifier: MIT
 */
package test;

import java.util.Locale;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.function.Executable;

import word2number.W2N;

/**
 * @author Sͬeͥbͭaͭsͤtͬian
 *
 */
class English {

  @BeforeAll
  static void setUpBeforeClass() throws Exception {
    Locale.setDefault(Locale.ENGLISH);
  }
  
  @Test
  final void testPositives_en() {
      Assertions.assertEquals(new W2N().wordToNum("two million three thousand nine hundred and eighty four"), 2003984);
      Assertions.assertEquals(new W2N().wordToNum("nineteen"), 19);
      Assertions.assertEquals(new W2N().wordToNum("two thousand and nineteen"), 2019);
      Assertions.assertEquals(new W2N().wordToNum("two million three thousand and nineteen"), 2003019);
      Assertions.assertEquals(new W2N().wordToNum("three billion"), 3000000000L);
      Assertions.assertEquals(new W2N().wordToNum("three million"), 3000000);
      Assertions.assertEquals(new W2N().wordToNum("one hundred twenty three million four hundred fifty six thousand seven hundred and eighty nine"), 123456789);
      Assertions.assertEquals(new W2N().wordToNum("eleven"), 11);
      Assertions.assertEquals(new W2N().wordToNum("nineteen billion and nineteen"), 19000000019L);
      Assertions.assertEquals(new W2N().wordToNum("one hundred and forty two"), 142);
      Assertions.assertEquals(new W2N().wordToNum("112"), 112);
      Assertions.assertEquals(new W2N().wordToNum("11211234"), 11211234);
      Assertions.assertEquals(new W2N().wordToNum("five"), 5);
      Assertions.assertEquals(new W2N().wordToNum("two million twenty three thousand and forty nine"), 2023049);
      Assertions.assertEquals(new W2N().wordToNum("two point three"), 2.3);
      Assertions.assertEquals(new W2N().wordToNum("two million twenty three thousand and forty nine point two three six nine"), 2023049.2369);
      Assertions.assertEquals(new W2N().wordToNum("one billion two million twenty three thousand and forty nine point two three six nine"), 1002023049.2369);
      Assertions.assertEquals(new W2N().wordToNum("point one"), 0.1D);
      Assertions.assertEquals(new W2N().wordToNum("point"), 0);
      Assertions.assertEquals(new W2N().wordToNum("point nineteen"), 0);
      Assertions.assertEquals(new W2N().wordToNum("one hundred thirty-five"), 135);
      Assertions.assertEquals(new W2N().wordToNum("hundred"), 100);
      Assertions.assertEquals(new W2N().wordToNum("thousand"), 1000);
      Assertions.assertEquals(new W2N().wordToNum("million"), 1000000);
      Assertions.assertEquals(new W2N().wordToNum("billion"), 1000000000);
      Assertions.assertEquals(new W2N().wordToNum("one million and thousand"), 1_001_000);
      Assertions.assertEquals(new W2N().wordToNum("nine point nine nine nine"), 9.999);
      Assertions.assertEquals(new W2N().wordToNum("seventh point nineteen"), 0);
      Assertions.assertEquals(new W2N().wordToNum("seven million, eight hundred, and sixty three thousand, two hundred, and fifty four"), 7863254);

      // test cases https://github.com/akshaynagpal/w2n/issues/54
      Assertions.assertEquals(new W2N().wordToNum("three point nine seven"), 3.97);
      Assertions.assertEquals(new W2N().wordToNum("two point seven eight"), 2.78);
      Assertions.assertEquals(new W2N().wordToNum("one point eight six"), 1.86);
      Assertions.assertEquals(new W2N().wordToNum("two point seven two"), 2.72);
      Assertions.assertEquals(new W2N().wordToNum("one point eight four"), 1.84);
      Assertions.assertEquals(new W2N().wordToNum("two point two eight"), 2.28);
      Assertions.assertEquals(new W2N().wordToNum("two point four seven"), 2.47);
      Assertions.assertEquals(new W2N().wordToNum("one point five nine"), 1.59);
      
      // test for kylosnite repository
      Assertions.assertEquals(new W2N().wordToNum("nine million nine thousand"), 9009000);

      // in different to w2n it is ok, in result of str:112 is not different to int:112
      Assertions.assertEquals(new W2N().wordToNum("112"), 112);
      Assertions.assertEquals(new W2N().wordToNum(112),112);
    
  }
  
  @Test
  final void testNull_en() {
    Assertions.assertThrows(NumberFormatException.class, new Executable() {
      public void execute() throws Throwable {
        new W2N().wordToNum((String)null);
      }
    });
    Assertions.assertThrows(NumberFormatException.class, new Executable() {
      public void execute() throws Throwable {
        new W2N().wordToNum((Number)null);
      }
    });
    Assertions.assertThrows(NumberFormatException.class, new Executable() {
      public void execute() throws Throwable {
        new W2N().wordToNum("");
      }
    });
  }

  @Test
  final void testNegatives_en() {
    String [] failValues = new String [] {
      "112-",
      "-",
      "on",
      "million million",
      "three million million",
      "million four million",
      "thousand million",
      "one billion point two million twenty three thousand and forty nine point two three six nine",
    };
    for (String failValue : failValues) {
      Assertions.assertThrows(NumberFormatException.class, () -> {
        new W2N().wordToNum(failValue);
      });
    }
    // type safe language, do not test:
    //self.assertRaises(ValueError, w2n.word_to_num, 112)
  }
  
  /*
  @AfterAll
  static void tearDownAfterClass() throws Exception {
  }

  @BeforeEach
  void setUp() throws Exception {
  }

  @AfterEach
  void tearDown() throws Exception {
  }
   */
  
}
