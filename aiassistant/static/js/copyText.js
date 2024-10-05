const copyButton = document.querySelector('copy-button');
const textToCopy = document.querySelector('.text-to-copy');

copyButton.addEventListener('click', () => {
    text = textToCopy.innerText
    copyContent(text);
})

const copyContent = async (text) => {
    try {
      await navigator.clipboard.writeText(text);
      console.log('Tekst skopiowany');
    } catch (err) {
      console.error('Błąd kopiowania: ', err);
    }
}