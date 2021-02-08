/**
 * SPDX-FileCopyrightText: 2021 - Sebastian Ritter <bastie@users.noreply.github.com>
 * SPDX-License-Identifier: MIT
 */
using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Reflection;
using System.Text;
using System.Text.RegularExpressions;

namespace word2number
{
    /// <summary> 
    ///Word2Number implementation
    ///
    /// This class implements an easy algorithm to translate number words to numbers from sentences.
    /// It takes a String instances and returns as result null or an 
    /// Number instance.
    /// 
    /// <br/>Author: Sͬeͥbͭaͭsͤtͬian
    /// </summary>
    public class W2N {
        private readonly Dictionary<String, Object> numberSystem;
        private readonly Dictionary<String, String> normalizeData;
        private readonly List<String> decimalWords;
        private readonly List<long> sortedMeasureValues;
  
  private readonly String lang;
  
  public W2N () {
    String newLang = null;
    if (Environment.GetEnvironmentVariable("w2n.lang") != null)
    newLang = Environment.GetEnvironmentVariable("w2n.lang");
    if (newLang == null)
        newLang = CultureInfo.CurrentCulture.TwoLetterISOLanguageName;
    if (newLang == null)
    if (Environment.GetEnvironmentVariable("LANGUAGE") != null)
        newLang = Environment.GetEnvironmentVariable("LANGUAGE");
    if (newLang == null)
        newLang = "en";  // fallback
    this.lang = newLang.Substring(0,2);

    this.numberSystem = new Dictionary<string, object>();
    this.decimalWords = new List<String>(10);
    this.normalizeData = new Dictionary<string, string>();
    this.sortedMeasureValues = new List<long>();
    
    var fileStream = Assembly.GetExecutingAssembly().GetManifestResourceStream("W2N.data.config_"+lang+".properties");;
    using (var streamReader = new StreamReader(fileStream, Encoding.UTF8)) {
      String line = null;
      int zeroToNine = 0;
      while ((line = streamReader.ReadLine()) != null)
      {
        if (line.StartsWith("#")) {
        }
        else {
            String[] keyValue = line.Split("=",2);
            String key = keyValue[0];
            Object val = keyValue[1];
            if (key.StartsWith("replace:")) {
              key = key.Substring("replace:".Length);
              normalizeData.Add(key,val.ToString().Trim());
            }
            else if (key.StartsWith("measure:")) {
              long.TryParse(val.ToString().Trim(), out long value);
              sortedMeasureValues.Add(value);
            }
            else if (!"point".Equals(key)) {
              long.TryParse(val.ToString().Trim(), out long value);
              val = value;
            }
            if (!key.StartsWith("replace:") && !key.StartsWith("measure:")) {
              this.numberSystem.Add(key, val);
            }
            if (zeroToNine<10) {
              this.decimalWords.Add(key);
              zeroToNine++;
            }
        }
      }
    }
    sortedMeasureValues.Sort();
    sortedMeasureValues.Reverse();
  }
  

  /**
   * Method to form numeric multipliers for million, billion, thousand etc.
   * @param numberWords list of strings
   * @return value: integer
   */
  protected int numberFormation (List<String> numberWords) {

    List<int> digitValues = new List<int>();
    // calculate the three digit values (max)
    foreach (String word in numberWords) {
        int nextNumberCandidat = 0;
        int.TryParse(this.numberSystem[word].ToString(), out nextNumberCandidat);
        digitValues.Add(nextNumberCandidat);
    }
    int hundredIndex = digitValues.Contains(100) ? digitValues.IndexOf(100) : -1;
    if (hundredIndex == 1){
        digitValues[0] =  digitValues[0] * digitValues [1]; // this is equals to Python
        digitValues.Remove(digitValues[1]);
    }
    if ((digitValues.Count > 3) && (digitValues[0] < 100)) {
      digitValues[0] *= digitValues[1];
      digitValues.Remove(digitValues[1]);
    }
    else if ((digitValues.Count > 3) && (digitValues[0] > 100)) {
        digitValues[1] *= digitValues[2];
        digitValues.Remove(digitValues[2]);
    }
    // add the three digits
    while (digitValues.Count > 1) {
        digitValues[0] += digitValues[1];
        digitValues.Remove(digitValues[1]);
    }
    // return the result

    return digitValues[0];
  }

  /**
   * Method to convert post decimal digit words to numerial digits
   * it returns a string to prevert from floating point conversation problem
   * @param decimalDigitWords list of strings
   * @return string
   */
  protected String getDecimalString(List<String> decimalDigitWords) {
    String decimalNumberStr = ""; 
    foreach (String decWord in decimalDigitWords) {
      if(!decimalWords.Contains(decWord))
        return "0";
      else
        decimalNumberStr += this.numberSystem[decWord];
    }
    String finalDecimalString = decimalNumberStr; // TODO remove line
    return finalDecimalString;
  }
  
  /**
   * function to return integer for an input `newNumberValue` string
   * @param newNumberValue numberValue
   * @return Number or null
   */
  public long wordToNum (long newNumberValue) {
    return newNumberValue;
  }
  
  /**
   * Method to return integer for an input `newObjectToStringIsNumeric` string
   * @param newObjectToStringIsNumeric
   * @return Number or null
   */
  protected dynamic wordToNum (Object newObjectToStringIsNumeric) {
    if (null == newObjectToStringIsNumeric)
      throw new FormatException("Type of input is not string! Please enter a valid number word (eg. \'two million twenty three thousand and forty nine\')");
    else 
      return this.wordToNum(newObjectToStringIsNumeric.ToString());
  }
  /**
   * Method to return integer for an input `newNumberSentence` string
   * @param numberSentence text
   * @return Number, prefered Long and Double, or null
   */
  public dynamic wordToNum (String newNumberSentence) {
    dynamic result = null;
    List<String> cleanNumbers = new List<String>();
    List<String> cleanDecimalNumbers = new List<String>();

    if (null == newNumberSentence)
      throw new FormatException("Type of input is null! Please enter a valid number word (eg. \'two million twenty three thousand and forty nine\')");

    String numberSentence = this.normalize(newNumberSentence.ToString());

    // return the number if user enters a number string
    long tempLong;
    if (long.TryParse(numberSentence, out tempLong)) {
        result = tempLong;
    }
    else {
        double tempDouble;
        if (double.TryParse(numberSentence, out tempDouble)) {
            result = tempDouble;
        }
    }

    bool isDigit = result != null; // maybe to optimize by compiler but to similar code to python 
    if (!isDigit) {
      String [] splitWords = Regex.Split(numberSentence,"[\\s,]+"); // strip extra spaces and comma and than split sentence into words
      String localizedPointName = this.numberSystem["point"].ToString();
      
      // removing and, & etc.
      foreach (String word in splitWords) {
        if (this.numberSystem.ContainsKey(word)) {
          cleanNumbers.Add(word);
        }
        else if (word.Equals(localizedPointName)){
          cleanNumbers.Add(word);
        }
      }

  
      // Error message if the user enters invalid input!
      if (cleanNumbers.Count== 0) 
          throw new FormatException("No valid number words found! Please enter a valid number word (eg. two million twenty three thousand and forty nine)");

      bool toMuchPoints = cleanNumbers.IndexOf(localizedPointName) != cleanNumbers.LastIndexOf(localizedPointName);
      if (toMuchPoints)
        throw new FormatException(String.Format("Redundant point word {0}! Please enter a valid number word (eg. two million twenty three thousand and forty nine)",localizedPointName));
  
      // separate decimal part of number (if exists)
      bool pointCount = cleanNumbers.IndexOf(localizedPointName)>-1;
      if (pointCount) {
        cleanDecimalNumbers = new List<String>(cleanNumbers.GetRange(cleanNumbers.IndexOf(localizedPointName)+1, cleanNumbers.Count-(cleanNumbers.IndexOf(localizedPointName)+1))); //#1
        cleanNumbers = new List<String>(cleanNumbers.GetRange(0,cleanNumbers.IndexOf(localizedPointName)));
      }

      // special case "point" without pre or post number   
      if (cleanDecimalNumbers.Count == 0 && cleanNumbers.Count == 0) return (int) 0;

      // check measure word errors
      List<int> measureWordsSequence = new List<int>();
      // check for to much measure words like "million million"
      foreach (long measureValueDoubleCheck in sortedMeasureValues) {
        if (measureValueDoubleCheck >= 1000) { // measure values under 1000 can be more than one in text
          checkDoubleInput(measureValueDoubleCheck, cleanNumbers);
          // save index for next check
          if (-1 != getIndexForNumber(measureValueDoubleCheck,cleanNumbers)){
            measureWordsSequence.Add(getIndexForNumber(measureValueDoubleCheck,cleanNumbers));
          }
        }
      }
      
      List<int> sortedMeasureWordsSequence = new List<int>(measureWordsSequence);
      sortedMeasureWordsSequence.Sort();
      for (int i = 0; i <measureWordsSequence.Count;i++) {
        if (!measureWordsSequence[i].Equals(sortedMeasureWordsSequence[i])) {
          throw new FormatException ("Malformed number in result of false measure word sequence eg. trillion after thousand! Please enter a valid number word (eg. two million twenty three thousand and forty nine)");
        }
      }
      
      // normalize measure words with add localized value for 1 before than empty
      bool lastWasMeasureWord = true;
      List<String> normalizedCleanNumbers = new List<String>(); 
      List<String> measureNames = new List<String>();
      foreach (long value in sortedMeasureValues) {
        measureNames.Add(getNameByNumberValue(value));
      }
      foreach (String nextPart in cleanNumbers) {
        if (measureNames.Contains(nextPart) && lastWasMeasureWord) {
          normalizedCleanNumbers.Add(this.getNameByNumberValue(1L));
          lastWasMeasureWord = true;
        }
        else {
          lastWasMeasureWord = measureNames.Contains(nextPart); 
        }
        normalizedCleanNumbers.Add(nextPart);
      }
      cleanNumbers = normalizedCleanNumbers;


      // check no measure words in decimal numbers
      foreach (long measureValue in sortedMeasureValues) {
          String measure_name = getNameByNumberValue(measureValue);
          if (cleanDecimalNumbers.Contains(measure_name))
            throw new FormatException ("Malformed number in result of false measure word after point eg. trillion after thousand! Please enter a valid number word (eg. two million twenty three thousand and forty nine)");
      }
      
      // Now we calculate the pre-decimal value
      result = getNumberValue(cleanNumbers);
 
      // And add the post-decimal value
      if (cleanDecimalNumbers.Count > 0){
        String decimalValue = getDecimalString(cleanDecimalNumbers);
        decimalValue = ""+result+"."+decimalValue;
        if (decimalValue.Substring(decimalValue.IndexOf(".")).Equals(".0")) {
          decimalValue = decimalValue.Substring(0, decimalValue.IndexOf("."));
          long.TryParse (decimalValue,out tempLong);
          result = tempLong;
          if (tempLong < int.MaxValue &&
              tempLong > int.MinValue) {
            result = (int)tempLong;
          }
        }
        else {
            double tempDouble;
            double.TryParse (decimalValue, NumberStyles.Any,CultureInfo.InvariantCulture, out tempDouble);
            result = tempDouble;
        }
      }
    }
    if (result is long) {
        tempLong = (long) result;
        if (tempLong < int.MaxValue &&
            tempLong > int.MinValue) {
            result = (int)tempLong;
        }
    }    

    return result;
  }
  

  /**
   * Method to normalize the whole(!) input text
   * @param numberSentence input string
   * @return normalized input
   */ 
  protected String normalize(String numberSentence) {
    numberSentence = numberSentence.ToLower(new CultureInfo(this.lang));  // converting input to lowercase
    numberSentence = numberSentence.Replace ("-"," ");

    // for examples: both is right "vingt et un" and "vingt-et-un"
    // we change this to composed value "vingt-et-un" over the localized data file "replace:" entry
    foreach (KeyValuePair<String, String> nonAndComposedNumber in this.normalizeData) {
      if (nonAndComposedNumber.Key.Contains(" ")) {
        numberSentence = numberSentence.Replace(nonAndComposedNumber.Key, nonAndComposedNumber.Value);
      }
    }
    
    return numberSentence.Trim();
  }
  
  
  /**
   * Method to check false redundant input
   *
   * <br/> Note: call this after normalize (lemma,replace,...) text
   * 
   * @param int new_number, string[] words - looking for count of localized name of new_numerb in words
   * @throws FormatException if redundant input error
   * @implNote this method has language configuration dependency
   * <br/> example 1: check_double_input (1000, "thousand thousand") with lang="en" throws a FormatException
   * <br/> example 2: check_double_input (1000, "thousand thousand") with lang="de" its ok
   * <br/> example 3: check_double_input (1000, "tausend tausend") with lang="de" throws a FormatException
   */
  protected void checkDoubleInput(long newNumber, List<String> cleanNumbers) {
    String localizedName =  this.getNameByNumberValue(newNumber);
    
    bool countGreaterOne = cleanNumbers.IndexOf(localizedName) != cleanNumbers.LastIndexOf(localizedName);
    if (countGreaterOne)
        throw new FormatException (String.Format("Redundant number word {0} in! Please enter a valid number word (eg. two million twenty three thousand and forty nine)",localizedName));
  }
  

  /**
   * Method to get the value for the measure aka 1000, 1_000_000 ...
   * @param measureIndex index of measure
   * @param cleanNumbers
   * @return multiplier for measure
   */
  protected long getMeasureMultiplier (int measureIndex, List<String> cleanNumbers) {
    List<String> param = cleanNumbers.GetRange(0,measureIndex);
    if (param.Count == 0) {
      param.Add(this.getNameByNumberValue(1L));
    }
    long multiplier = this.numberFormation(param);
    return multiplier;
  }

  /**
   * Method to get the localized name form value
   * @param newNumber numeric value
   * @return name from language configuration or <code>null</code> if not found 
   */
  protected String getNameByNumberValue (long newNumber) {
    foreach (KeyValuePair<string, object> pair in this.numberSystem) {
      String numberString = ""+newNumber;
      if (numberString.Equals(pair.Value.ToString())) {
        return pair.Key;
      }
    }
    return null;
  }
  
  /**
   * Method to get the index of name for given number
   * 
   * <br/> note: call this after normalize (lemma,replace,...) text
   * 
   * @param newNumber number to looking for
   * @param cleanNumbers
   * @return index or -1 if not found
   */
  protected int getIndexForNumber (long newNumber, List<String> cleanNumbers) {
    String localizedName = getNameByNumberValue(newNumber);
    return cleanNumbers.IndexOf(localizedName);
  }
  
  /**
   * Method to get the pre-decimal number from clean_number
   * @param sorted list with number words
   * @return number
   */
      protected long getNumberValue (List<String> cleanNumbers) {
        long result = 0L;

        /*
        * The simple algorithm based on the idea from NLP to work with tagging (key)words
        * but yes it is handmade implemented today.
        *
        * -- 2021-02-05 --
        * The tagging can be tested on for example https://parts-of-speech.info and tell for
        * nine trillion one billion two million twenty three thousand and forty nine point two three six nine
        * - "and" is a conjunction
        * - "point" is a none
        * - all other are numbers
        * But also contains this line these "measure words" for numbers:
        * - trillion
        * - billion
        * - million
        * - thousand
        * - hundred
        * This new algorithm split the word array from highest value to lowest 
        * (because hundred can be a measure and also a number). Then it work
        * only with number for this measure, simplify so the algorithm and
        * make it free from other measure part in the number.
        * Also it is no different to calculate a trillion or a million or other
        */
        foreach (long measureValue in sortedMeasureValues){
          int measureValueIndex = getIndexForNumber(measureValue, cleanNumbers);
          if (measureValueIndex > -1){
            result +=  getMeasureMultiplier(measureValueIndex, cleanNumbers) * measureValue;
            cleanNumbers = cleanNumbers.GetRange(measureValueIndex+1,cleanNumbers.Count-(measureValueIndex+1)); //#1
          }
        }
        // Now we add the value of less then hundred
        if (cleanNumbers.Count > 0){
          int multiplier = this.numberFormation(cleanNumbers);
          result +=  multiplier * 1;
        }

        return result;
      }
  }
}
