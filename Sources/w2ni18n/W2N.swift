/**
 * SPDX-FileCopyrightText: 2025 - Sebastian Ritter <bastie@users.noreply.github.com>
 * SPDX-License-Identifier: MIT
 */

import JavApi
import Foundation

/**
 * 
 * Word2Number implementation
 * 
 * This class implements an easy algorithm to translate number words to numbers from sentences.
 * It takes a <code>CharSequence</code> like <code>String</code>, <code>StringBuilder</code> or 
 * <code>StringBuffer</code> instances and returns as result <code>null</code> or an 
 * <code>Number</code> instance.
 * On other Objects the <code>toString</code> method is using to create a CharSequence on-the-fly.
 * 
 * @author Sͬeͥbͭaͭsͤtͬian
 *
 */
open class W2N {
  
  /**
   * The localized number system.
   */
  private var numberSystem : java.util.HashMap<String, Int64>
  private var normalizeData : java.util.HashMap<String, String>
  /**
   * The decimal words are ever the first ten words in config file.
   */
  private var decimalWords : [String]
  /**
   * The measure values
   */
  private var sortedMeasureValues : [Int64]
  /**
   * The localized name of point, for example "komma" in german
   */
  private let localizedPointName : String
  
  /**
   * The language 
   */
  private let lang : String
  
  /**
   * Construct new W2N instance with optional parameter for language.
   * @param langParam optional language parameter
   */
  public init (_ langParam : String...) throws {
    do {
      var newLang : String? = nil
      if (langParam.length > 0) {
        newLang = langParam[0]
      }
      if (System.getenv("w2n.lang") != nil) {
        newLang = System.getenv("w2n.lang")
      }
      if (newLang == nil) {
        newLang = java.util.Locale.getDefault().getLanguage()
      }
      if (newLang == nil) {
        if (System.getenv("LANGUAGE") != nil) {
          newLang = System.getenv("LANGUAGE")
        }
      }
      if (newLang == nil) {
        newLang = "en"  // fallback
      }
      self.lang = newLang!.substring(0,2);
  
      self.numberSystem = java.util.HashMap<String, Int64>()
      self.decimalWords = Array.init(repeating: "", count: 10)
      self.normalizeData = java.util.HashMap<String, String>()
      self.sortedMeasureValues = [Int64]()
      let resourceName = "config_\(self.lang)"
      let resource = Bundle.module.url(forResource: resourceName, withExtension: "properties")!
      let content = try String(contentsOf: resource, encoding: .utf8)
      let lines = content.components(separatedBy: .newlines)
      
      var zeroToNine = 0
      var pointName = ""
      for line in lines {
          if (line.startsWith("#")) {
          }
        else {
          let keyValue = line.split(separator: "=", maxSplits: 1).map(String.init) // var keyValue = line.split("=",2)
          var key = keyValue[0].trim()
          let val = keyValue[1].trim()
          if (key.startsWith("replace:")) {
            key = key.substring("replace:".count)
            _ = normalizeData.put(key,val.toString().trim())
          }
          else if (key.startsWith("measure:")) {
            _ = sortedMeasureValues.add(Int64(val.toString().trim())!) // maybe throws error
          }
          else if ("point".equals(key)) {
            pointName = val
          }
          else {
            _ = self.numberSystem.put(key, Int64(val.toString().trim())!) // maybe throws error
          }
          if (zeroToNine<10) {
            _ = self.decimalWords.add(key)
            zeroToNine += 1
          }
        }
      }
      self.localizedPointName = pointName;
      sortedMeasureValues.sort(by: >) //Collections.sort(sortedMeasureValues,Collections.reverseOrder());
    }
    catch  {
      throw RuntimeException(error.localizedDescription);
    }
  }
  
  /**
   * Method to form numeric multipliers for million, billion, thousand etc.
   * @param numberWords list of strings
   * @return value: integer
   */
  open func numberFormation (_ numberWords : [String]) -> Int {
    var digitValues : [Int] = []
    // calculate the three digit values (max)
    for word in numberWords {
      let nextNumberCandidat : Int = Int(self.numberSystem.get(word)!);
        _ = digitValues.add(nextNumberCandidat);
    }
    
    let hundredIndex = digitValues.contains(100) ? digitValues.firstIndex(of: 100)! : -1
    if (hundredIndex == 1){
      //digitValues.set(0, digitValues.get(0) * digitValues.get(1));
      digitValues[0] = digitValues[0] * digitValues[1]
      //digitValues.remove(1);
      digitValues.remove(at: 1)
    }
    if ((digitValues.count > 3) && (digitValues[0] < 100)) {
      //digitValues.set(0, digitValues.get(0) * digitValues.get(1));
      digitValues[0] = digitValues[0] * digitValues[1]
      //digitValues.remove(1);
      digitValues.remove(at: 1)
    }
    else if ((digitValues.count > 3) && (digitValues[0] > 100)) {
      //digitValues.set(1,digitValues.get(1) * digitValues.get(2));
      digitValues[1] = digitValues[1] * digitValues[2]
      //digitValues.remove(2);
      digitValues.remove(at: 2)
    }
    // add the three digits
    while (digitValues.count > 1) {
      //digitValues.set(0, digitValues.get(0) + digitValues.get(1));
      digitValues[0] = digitValues[0] + digitValues[1]
      //digitValues.remove(1);
      digitValues.remove(at: 1)
    }
    // return the result
    return digitValues[0]
  }

  /**
   * function to convert post decimal digit words to numerial digits
   * it returns a string to prevert from floating point conversation problem
   * @param decimalDigitWords list of strings
   * @return string
   */
  open func getDecimalString(_ decimalDigitWords : [String]) -> String {
    var decimalNumberStr = ""; // TODO: check python in result of do not need an array in Java
    for decWord in decimalDigitWords {
      if(!decimalWords.contains(decWord)) {
        return "0"
      }
      else {
        decimalNumberStr += "\(numberSystem.get(decWord)!)"
      }
    }
    return decimalNumberStr
  }
  
  /**
   * function to return integer for an input `newNumberValue` string
   * @param newNumberValue numberValue
   * @return Number or null
   */
  open func wordToNum (_ newNumberValue : any Numeric) -> any Numeric {
    return newNumberValue;
  }
  
  /**
   * Method to return integer for an input `newObjectToStringIsNumeric` string
   * @param newObjectToStringIsNumeric
   * @return Number or null
   */
  open func wordToNum (_ newObjectToStringIsNumeric : Any) throws -> any Numeric {
    return try self.wordToNum("\(newObjectToStringIsNumeric)");
  }
  /**
   * Method to return integer for an input `newNumberSentence` string
   * @param numberSentence text
   * @return Number, prefered Long and Double, or null
   */
  open func wordToNum (_ newNumberSentence : String) throws -> any Numeric {
    var result : (any Numeric)? = nil
    var cleanNumbers = [String]()
    var cleanDecimalNumbers = [String]()

    let numberSentence : String = self.normalize(newNumberSentence.toString());

    // return the number if user enters a number string
    let formatter = NumberFormatter()
    formatter.locale = java.util.Locale.getDefault().delegate
    if let number = formatter.number(from: newNumberSentence) {
      // Prüfe, ob die Zahl ganzzahlig ist
      if number.doubleValue == Double(number.int64Value) {
        result = number.int64Value // Speichere als Int64
      } else {
        result = number.doubleValue // Speichere als Double
      }
    }
    let isDigit : Bool = result != nil; // maybe to optimize by compiler but to similar code to python
    if (!isDigit) {
      let splitWords = numberSentence.components(separatedBy: CharacterSet(charactersIn: ",").union(.whitespaces)).filter { !$0.isEmpty }
      // removing and, & etc.
      for word in splitWords {
        if (self.numberSystem.containsKey(word)) {
          _ = cleanNumbers.add(word);
        }
        else if (word.equals(self.localizedPointName)){
          _ = cleanNumbers.add(word);
        }
      }
  
      // Error message if the user enters invalid input!
      if (cleanNumbers.count == 0) {
        throw NumberFormatException("No valid number words found! Please enter a valid number word (eg. two million twenty three thousand and forty nine)")
      }

      let toMuchPoints = cleanNumbers.indexOf(self.localizedPointName) != cleanNumbers.lastIndexOf(localizedPointName);
      if (toMuchPoints) {
        throw NumberFormatException("Redundant point word \(localizedPointName)! Please enter a valid number word (eg. two million twenty three thousand and forty nine)")
      }
  
      // separate decimal part of number (if exists)
      let pointCount = cleanNumbers.indexOf(self.localizedPointName) > -1;
      if (pointCount) {
        let indexPlus1 = cleanNumbers.indexOf(self.localizedPointName) + 1
        cleanDecimalNumbers = Array(cleanNumbers[indexPlus1..<cleanNumbers.count])
        cleanNumbers = Array(cleanNumbers[0..<cleanNumbers.indexOf(self.localizedPointName)])
      }
      // special case "point" without pre or post number   
      if (cleanDecimalNumbers.count == 0 && cleanNumbers.count == 0) {
        return Int(0)
      }

      // check measure word errors
      var measureWordsSequence = [Int]()
      // check for to much measure words like "million million"
      for measureValueDoubleCheck in sortedMeasureValues {
        if (measureValueDoubleCheck >= 1000) { // measure values under 1000 can be more than one in text
          try checkDoubleInput(measureValueDoubleCheck, cleanNumbers);
          // save index for next check
          if (-1 != getIndexForNumber(measureValueDoubleCheck,cleanNumbers)){
            _ = measureWordsSequence.add(getIndexForNumber(measureValueDoubleCheck,cleanNumbers))
          }
        }
      }
      
      var sortedMeasureWordsSequence = measureWordsSequence
      sortedMeasureWordsSequence.sort()
      for i in 0..<measureWordsSequence.count {
        if (measureWordsSequence[i] != sortedMeasureWordsSequence[i]) {
          throw NumberFormatException ("Malformed number in result of false measure word sequence eg. trillion after thousand! Please enter a valid number word (eg. two million twenty three thousand and forty nine)");
        }
      }
      
      // normalize measure words with add localized value for 1 before than empty
      var lastWasMeasureWord = true;
      var normalizedCleanNumbers = [String]()
      var measureNames = [String]()
      for value in sortedMeasureValues {
        _ = measureNames.add(getNameByNumberValue(value)!);
      }
      for nextPart in cleanNumbers {
        if (measureNames.contains(nextPart) && lastWasMeasureWord) {
          _ = normalizedCleanNumbers.add(self.getNameByNumberValue(1)!);
          lastWasMeasureWord = true;
        }
        else {
          lastWasMeasureWord = measureNames.contains(nextPart); 
        }
        _ = normalizedCleanNumbers.add(nextPart);
      }
      cleanNumbers = normalizedCleanNumbers;


      // check no measure words in decimal numbers
      for measureValue in sortedMeasureValues {
        let measure_name = getNameByNumberValue(measureValue)!
        if (cleanDecimalNumbers.contains(measure_name)) {
          throw NumberFormatException ("Malformed number in result of false measure word after point eg. trillion after thousand! Please enter a valid number word (eg. two million twenty three thousand and forty nine)")
        }
      }
      
      // Now we calculate the pre-decimal value
      result = getNumberValue(cleanNumbers);
      
      // And add the post-decimal value
      if (cleanDecimalNumbers.count > 0){
        var decimalValue = getDecimalString(cleanDecimalNumbers)
        decimalValue = "\(result ?? 0).\(decimalValue)"
        // Prüfe, ob der String auf ".0" endet
        if decimalValue.hasSuffix(".0") {
          // Entferne ".0" und konvertiere zu Int64 (Long in Java)
          if let longValue = Int64(decimalValue.replacingOccurrences(of: ".0", with: "")) {
            // Prüfe, ob der Wert in den Int32 (Integer)-Bereich passt
            if longValue >= Int64(Int32.min) && longValue <= Int64(Int32.max) {
              result = Int(longValue)
            } else {
              result = longValue
            }
          }
        } else {
          // Konvertiere zu Double, falls Nachkommastellen vorhanden sind
          if let doubleValue = Double(decimalValue) {
            result = doubleValue
          }
        }
      }
    }
    return result!
  }
  

  /**
   * Method to normalize the whole(!) input text
   * @param numberSentence input string
   * @return normalized input
   */
  open func normalize(_ numberSentence : String) -> String {
    var numberSentence = numberSentence
    numberSentence = numberSentence.lowercased(with: java.util.Locale(self.lang).delegate) // converting input to lowercase
    numberSentence = numberSentence.replace ("-"," ");

    // for examples: both is right "vingt et un" and "vingt-et-un"
    // we change this to composed value "vingt-et-un" over the localized data file "replace:" entry
    for nonComposedNumberValue in self.normalizeData.delegate.keys {
      if (nonComposedNumberValue.contains(" ")) {
        let composedNumberValue = self.normalizeData.get(nonComposedNumberValue);
        numberSentence = numberSentence.replace(nonComposedNumberValue, composedNumberValue!);
      }
    }
    // TODO: CHECK: Why run Python without next part?
    var result = ""
    let words = numberSentence.components(separatedBy: .whitespaces.union(.punctuationCharacters))
      .filter { !$0.isEmpty }
    for var word in words {
      if (self.normalizeData.containsKey(word)) {
        word = self.normalizeData.get(word)!;
      }
      result += "\(word) ";
    }
    
    return result.trim();
  }
  
  
  /**
   * Method to check false redundant input
   *
   * <br/> Note: call this after normalize (lemma,replace,...) text
   * 
   * @param int new_number, string[] words - looking for count of localized name of new_numerb in words
   * @throws NumberFormatException if redundant input error
   * @implNote this method has language configuration dependency
   * <br/> example 1: check_double_input (1000, "thousand thousand") with lang="en" throws a NumberFormatException
   * <br/> example 2: check_double_input (1000, "thousand thousand") with lang="de" its ok
   * <br/> example 3: check_double_input (1000, "tausend tausend") with lang="de" throws a NumberFormatException
   */
  public func checkDoubleInput(_ newNumber : Int64, _ cleanNumbers : [String]) throws {
    let localizedName =  self.getNameByNumberValue(newNumber);
    
    let countGreaterOne = cleanNumbers.indexOf(localizedName) != cleanNumbers.lastIndexOf(localizedName);
    if (countGreaterOne) {
      throw NumberFormatException ("Redundant number word (\(localizedName ?? "???")) in! Please enter a valid number word (eg. two million twenty three thousand and forty nine)")
    }
  }
  

  /**
   * Method to get the value for the measure aka 1000, 1_000_000 ...
   * @param measureIndex index of measure
   * @param cleanNumbers
   * @return multiplier for measure
   */
  public func getMeasureMultiplier (_ measureIndex : Int, _ cleanNumbers : [String]) -> Int64 {
    var param = Array(cleanNumbers[0..<measureIndex])
    if (param.isEmpty) {
      _ = param.add(self.getNameByNumberValue(Int64(1))!); // maybe Int128 ?
    }
    let multiplier : Int64 = Int64(self.numberFormation(param));
    return multiplier;
  }

  /**
   * Method to get the localized name form value
   * @param newNumber numeric value
   * @return name from language configuration or <code>null</code> if not found 
   */
  public func getNameByNumberValue (_ newNumber : Int64) -> String?{
    for key in self.numberSystem.delegate.keys {
      if (newNumber == self.numberSystem.get(key)) {
        return key;
      }
    }
    return nil;
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
  public func getIndexForNumber (_ newNumber : Int64, _ cleanNumbers : [String]) -> Int {
    let localizedName = getNameByNumberValue(newNumber);
    return cleanNumbers.indexOf(localizedName);
  }
  
  /**
   * Method to get the pre-decimal number from clean_number
   * @param sorted list with number words
   * @return number
   */
  open func getNumberValue (_ cleanNumbers : [String]) -> Int64 {
    var cleanNumbers = cleanNumbers
    var result : Int64 = 0

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
    
    for measureValue in sortedMeasureValues {
      let measureValueIndex = getIndexForNumber(measureValue, cleanNumbers);
      if (measureValueIndex > -1){
        result +=  getMeasureMultiplier(measureValueIndex, cleanNumbers) * measureValue;
        cleanNumbers = Array(cleanNumbers[(measureValueIndex+1)..<cleanNumbers.count])
      }
    }
    // Now we add the value of less then hundred
    if (cleanNumbers.count > 0){
      let multiplier = numberFormation(cleanNumbers);
      result += Int64(multiplier * 1)
    }

    return result;
  }
}
