export const helpers = {
  getVowelsQuantity(text) {
    const vowels = 'aeiou';
    let counter = 0;
    console.log('typeof', typeof text)
    text.toLowerCase().split('').forEach((char) => {
      if (vowels.includes(char)) counter++;
    });
    return counter;
  }
}