import unittest
import sys
sys.path.append("..")

import bmi

class TestBmi(unittest.TestCase):
    def test_worksWithProperInputIntegerRoundsToTenthsNormal(self):
        result = bmi.calcBmi(5,10,165)
        self.assertEqual(result, "23.7 Normal")

    def test_worksWithProperInputIntegerRoundsToTenthsNormalDup(self):
        result = bmi.calcBmi(6, 2, 185)
        self.assertEqual(result, "23.8 Normal")

    def test_worksWithProperInputIntegerRoundsToTenthObese(self):
        result = bmi.calcBmi(6,2,240)
        self.assertEqual(result, "30.8 Obese")

    def test_worksWithProperInputIntegerRoundsToTenthsObeseDup(self):
        result = bmi.calcBmi(5,3,180)
        self.assertEqual(result, "31.9 Obese")

    def test_worksWithProperInputIntegerRoundsToTenthsUnderweight(self):
        result = bmi.calcBmi(5,10,120)
        self.assertEqual(result, "17.2 Underweight")

    def test_worksWithProperInputIntegerRoundsToTenthsUnderweightDup(self):
        result = bmi.calcBmi(5,2,70)
        self.assertEqual(result, "12.8 Underweight")

    def test_worksWithProperInputFloatRoundsToTenthsNormal(self):
        result = bmi.calcBmi(5,10,165.0)
        self.assertEqual(result, "23.7 Normal")

    def test_worksWithProperInputFloatRoundsToTenthsNormalDup(self):
        result = bmi.calcBmi(6, 2, 185.0)
        self.assertEqual(result, "23.8 Normal")

    def test_worksWithProperInputFloatRoundsToTenthsObese(self):
        result = bmi.calcBmi(6,2,240.0)
        self.assertEqual(result, "30.8 Obese")

    def test_worksWithProperInputFloatRoundsToTenthsObeseDup(self):
        result = bmi.calcBmi(5,3,180.0)
        self.assertEqual(result, "31.9 Obese")

    def test_worksWithProperInputFloatRoundsToTenthsUnderweight(self):
        result = bmi.calcBmi(5,10,120.0)
        self.assertEqual(result, "17.2 Underweight")

    def test_worksWithProperInputFloatRoundsToTenthsUnderweightDup(self):
        result = bmi.calcBmi(5,2,70.0)
        self.assertEqual(result, "12.8 Underweight")

    def test_tallerThanTwiceTheTallestPersonEver(self):
        result = bmi.calcBmi(18, 0, 165)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_tallerThanTwiceTheTallestPersonEverDup(self):
        result = bmi.calcBmi(20, 2, 400)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_shorterThanHalfTheShortestPersonEver(self):
        result = bmi.calcBmi(0, 10, 200)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_shorterThanHalfTheShortestPersonEverDup(self):
        result = bmi.calcBmi(0, 8, 290)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_heavierThanTwiceTheHeaviestPersonEver(self):
        result = bmi.calcBmi(5, 10, 1950)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_heavierThanTwiceTheHeaviestPersonEver(self):
        result = bmi.calcBmi(5, 10, 2000)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_lighterThanHalfTheLightestPersonEver(self):
        result = bmi.calcBmi(5, 10, 0.03125)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_lighterThanHalfTheLightestPersonEverDup(self):
        result = bmi.calcBmi(5, 10, 0.0002)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_moreThanTwelveInches(self):
        result = bmi.calcBmi(5, 13, 165)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_moreThanTwelveInchesDup(self):
        result = bmi.calcBmi(5, 15, 165)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_negativeInches(self):
        result = bmi.calcBmi(5, -2, 165)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_negativeInchesDup(self):
        result = bmi.calcBmi(5, -4, 165)
        self.assertEqual(result, "ERROR: Invalid Input")

#///////////////////////////////////////////////////////////////////////

    def test_firstInputFloat(self):
        result = bmi.calcBmi(5.0, 10, 165)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_firstInputFloatDup(self):
        result = bmi.calcBmi(5.3, 10, 165)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_secondInputFloat(self):
        result = bmi.calcBmi(5, 10.0, 165)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_secondInputFloatDup(self):
        result = bmi.calcBmi(5, 10.3, 165)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_firstAndSecondInputFloat(self):
        result = bmi.calcBmi(5.0, 10.0, 165)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_firstandSecondInputFloatDup(self):
        result = bmi.calcBmi(5.3, 10.3, 165)
        self.assertEqual(result, "ERROR: Invalid Input")

#//////////////////////////////////////////////////////////////////////////

    def test_firstInputString(self):
        result = bmi.calcBmi("wrong",10,165)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_firstInputStringDup(self):
        result = bmi.calcBmi("alsoWrong",10,165)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_secondInputString(self):
        result = bmi.calcBmi(5,"wrong",165)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_secondInputStringDup(self):
        result = bmi.calcBmi(5, "alsoWrong", 165)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_secondAndFirstInputString(self):
        result = bmi.calcBmi("wrong", "wrong", 165)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_secondAndFirstInputStringDup(self):
        result = bmi.calcBmi("alsoWrong","alsoWrong",165)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_thirdInputString(self):
        result = bmi.calcBmi(5,10,"wrong")
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_thirdInputStringDup(self):
        result = bmi.calcBmi(5,10,"alsoWrong")
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_thirdAndFirstInputString(self):
        result = bmi.calcBmi("wrong",10,"wrong")
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_thirdAndFirstInputStringDup(self):
        result = bmi.calcBmi("alsoWrong",10,"AlsoWrong")
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_thirdAndSecondInputString(self):
        result = bmi.calcBmi(5,"wrong","wrong")
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_thirdAndSecondInputStringDup(self):
        result = bmi.calcBmi(5,"alsoWrong","alsoWrong")
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_firstSecondAndThirdInputString(self):
        result = bmi.calcBmi("wrong","wrong","wrong")
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_firstSecondAndThirdInputStringDup(self):
        result = bmi.calcBmi("alsoWrong","alsoWrong","alsoWrong")
        self.assertEqual(result, "ERROR: Invalid Input")

#//////////////////////////////////////////////////////////////////

    def test_firstInputList(self):
        result = bmi.calcBmi([1],10,165)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_firstInputListDup(self):
        result = bmi.calcBmi([1,2],10,165)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_secondInputList(self):
        result = bmi.calcBmi(5,[1],165)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_secondInputListDup(self):
        result = bmi.calcBmi(5, [1,2], 165)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_secondAndFirstInputList(self):
        result = bmi.calcBmi([1], [1], 165)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_secondAndFirstInputListDup(self):
        result = bmi.calcBmi([1,2],[1,2],165)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_thirdInputList(self):
        result = bmi.calcBmi(5,10,[1])
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_thirdInputListDup(self):
        result = bmi.calcBmi(5,10,[1,2])
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_thirdAndFirstInputList(self):
        result = bmi.calcBmi([1],10,[1])
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_thirdAndFirstInputListDup(self):
        result = bmi.calcBmi([1,2],10,[1,2])
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_thirdAndSecondInputList(self):
        result = bmi.calcBmi(5,[1],[1])
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_thirdAndSecondInputListDup(self):
        result = bmi.calcBmi(5,[1,2],[1,2])
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_firstSecondAndThirdInputList(self):
        result = bmi.calcBmi([1],[1],[1])
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_firstSecondAndThirdInputListDup(self):
        result = bmi.calcBmi([1,2],[1,2],[1,2])
        self.assertEqual(result, "ERROR: Invalid Input")

#//////////////////////////////////////////////////////////////////

    def test_firstInputTuple(self):
        result = bmi.calcBmi((1,2),10,165)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_firstInputTupleDup(self):
        result = bmi.calcBmi((1,2,3),10,165)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_secondInputTuple(self):
        result = bmi.calcBmi(5,(1,2),165)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_secondInputTupleDup(self):
        result = bmi.calcBmi(5, (1,2,3), 165)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_secondAndFirstInputTuple(self):
        result = bmi.calcBmi((1,2), (1,2), 165)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_secondAndFirstInputTupleDup(self):
        result = bmi.calcBmi((1,2,3),(1,2,3),165)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_thirdInputTuple(self):
        result = bmi.calcBmi(5,10,(1,2))
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_thirdInputTupleDup(self):
        result = bmi.calcBmi(5,10,(1,2,3))
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_thirdAndFirstInputTuple(self):
        result = bmi.calcBmi((1,2),10,(1,2))
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_thirdAndFirstInputTupleDup(self):
        result = bmi.calcBmi((1,2,3),10,(1,2,3))
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_thirdAndSecondInputTuple(self):
        result = bmi.calcBmi(5,(1,2),(1,2))
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_thirdAndSecondInputTupleDup(self):
        result = bmi.calcBmi(5,(1,2,3),(1,2,3))
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_firstSecondAndThirdInputTuple(self):
        result = bmi.calcBmi((1,2),(1,2),(1,2))
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_firstSecondAndThirdInputTupleDup(self):
        result = bmi.calcBmi((1,2,3),(1,2,3),(1,2,3))
        self.assertEqual(result, "ERROR: Invalid Input")

#//////////////////////////////////////////////////////////////////

    def test_firstInputBoolean(self):
        result = bmi.calcBmi(True,10,165)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_firstInputBooleanDup(self):
        result = bmi.calcBmi(False,10,165)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_secondInputBoolean(self):
        result = bmi.calcBmi(5,True,165)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_secondInputBooleanDup(self):
        result = bmi.calcBmi(5, False, 165)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_secondAndFirstInputBoolean(self):
        result = bmi.calcBmi(True, True, 165)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_secondAndFirstInputBooleanDup(self):
        result = bmi.calcBmi(False,False,165)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_thirdInputBoolean(self):
        result = bmi.calcBmi(5,10,True)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_thirdInputBooleanDup(self):
        result = bmi.calcBmi(5,10,False)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_thirdAndFirstInputBoolean(self):
        result = bmi.calcBmi(True,10,True)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_thirdAndFirstInputBooleanDup(self):
        result = bmi.calcBmi(False,10,False)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_thirdAndSecondInputBoolean(self):
        result = bmi.calcBmi(5,True,True)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_thirdAndSecondInputBooleanDup(self):
        result = bmi.calcBmi(5,False,False)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_firstSecondAndThirdInputBoolean(self):
        result = bmi.calcBmi(True,True,True)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_firstSecondAndThirdInputBooleanDup(self):
        result = bmi.calcBmi(False,False,False)
        self.assertEqual(result, "ERROR: Invalid Input")

#//////////////////////////////////////////////////////////////////

    def test_firstInputDictionary(self):
        result = bmi.calcBmi({1:2,3:4},10,165)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_firstInputDictionaryDup(self):
        result = bmi.calcBmi({"A":1,"B":2},10,165)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_secondInputDictionary(self):
        result = bmi.calcBmi(5,{1:2,3:4},165)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_secondInputDictionaryDup(self):
        result = bmi.calcBmi(5, {"A":1,"B":2}, 165)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_secondAndFirstInputDictionary(self):
        result = bmi.calcBmi({1:2,3:4}, {1:2,3:4}, 165)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_secondAndFirstInputDictionaryDup(self):
        result = bmi.calcBmi({"A":1,"B":2},{"A":1,"B":2},165)
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_thirdInputDictionary(self):
        result = bmi.calcBmi(5,10,{1:2,3:4})
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_thirdInputDictionaryDup(self):
        result = bmi.calcBmi(5,10,{"A":1,"B":2})
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_thirdAndFirstInputDictionary(self):
        result = bmi.calcBmi({1:2,3:4},10,{1:2,3:4})
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_thirdAndFirstInputDictionaryDup(self):
        result = bmi.calcBmi({"A":1,"B":2},10,{"A":1,"B":2})
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_thirdAndSecondInputDictionary(self):
        result = bmi.calcBmi(5,{1:2,3:4},{1:2,3:4})
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_thirdAndSecondInputDictionaryDup(self):
        result = bmi.calcBmi(5,{"A":1,"B":2},{"A":1,"B":2})
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_firstSecondAndThirdInputDictionary(self):
        result = bmi.calcBmi({1:2,3:4},{1:2,3:4},{1:2,3:4})
        self.assertEqual(result, "ERROR: Invalid Input")

    def test_firstSecondAndThirdInputDictionaryDup(self):
        result = bmi.calcBmi({"A":1,"B":2},{"A":1,"B":2},{"A":1,"B":2})
        self.assertEqual(result, "ERROR: Invalid Input")

        
