// """Turn a phrase into Pig Latin.

// This takes a space-separated phrase and returns it in Pig Latin.

// Rules:

// 1. If the word begins with a consonant (not a, e, i, o, u),
//    move the first letter to the end and add 'ay'

// 2. If the word begins with a vowel, add 'yay' to the end

// For example:

//     >>> pig_latin('hello awesome programmer')
//     'ellohay awesomeyay rogrammerpay'

// """

// def pig_latin(phrase):
//     """Turn a phrase into pig latin.

//     There will be no uppercase letters or punctuation in the phrase.

//         >>> pig_latin('hello awesome programmer')
//         'ellohay awesomeyay rogrammerpay'
//     """

function pigLatin(phrase) {

    var wordList = phrase.split(' ');
    var vowelList = ['a','e','i','o','u'];
    var newPhrase = '';

    for (var i = 0; i < wordList.length; i++) {
        if (vowelList.includes(wordList[i][0])) {
            var currWord = wordList[i] + 'ay ';

            newPhrase += currWord;            
        }
        else {
            var firstLetter = wordList[i][0];
            var baseWord = wordList[i].slice(1);
            var currWord = baseWord + firstLetter + 'ay ';

            newPhrase += currWord;
        }
    }

    return newPhrase
}

console.log(pigLatin('hello awesome programmer'))