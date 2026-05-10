/**
 * SPDX-FileCopyrightText: 2021 - Sebastian Ritter <bastie@users.noreply.github.com>
 * SPDX-License-Identifier: MIT
 */
package test;

import java.lang.System.Logger.Level;
import java.util.Locale;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.function.Executable;

import word2number.W2N;

/**
 * @author Sͬeͥbͭaͭsͤtͬian
 * @since 1.2.0
 */
public class Slovak {
  @BeforeAll
  static void setUpBeforeClass() throws Exception {
    Locale.setDefault(new Locale("sk"));
    System.getLogger(Slovak.class.getPackageName()).log(Level.INFO, 
        String.format("Testsystem is %s with Java %s", "",System.getProperty("java.version")));
    
  }
  
  @Test
  final void testPositives_sk() {
    Assertions.assertEquals(new W2N("sk").wordToNum("devätnásť"), 19);
    Assertions.assertEquals(new W2N("sk").wordToNum("sto"), 100);
    Assertions.assertEquals(new W2N("sk").wordToNum("tisíc"), 1000);
    Assertions.assertEquals(new W2N("sk").wordToNum("tisíc jedna"), 1001);
    Assertions.assertEquals(new W2N("sk").wordToNum("tisíc jeden"), 1001);
  }
  @Test
  final void testNull_sk() {
    Assertions.assertThrows(NumberFormatException.class, new Executable() {
      public void execute() throws Throwable {
        new W2N("sk").wordToNum((String)null);
      }
    });
    Assertions.assertThrows(NumberFormatException.class, new Executable() {
      public void execute() throws Throwable {
        new W2N("sk").wordToNum((Number)null);
      }
    });
    Assertions.assertThrows(NumberFormatException.class, new Executable() {
      public void execute() throws Throwable {
        new W2N("sk").wordToNum("");
      }
    });
  }

  @Test
  final void testNegatives_sk() {
    String [] failValues = new String [] {
      "112-",
      "-",
      "on",
    };
    for (String failValue : failValues) {
      Assertions.assertThrows(NumberFormatException.class, () -> {
        new W2N("sk").wordToNum(failValue);
      });
    }
    // type safe language, do not test:
    //self.assertRaises(ValueError, w2n.word_to_num, 112)
  }

}

//EOF