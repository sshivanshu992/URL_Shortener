

$(document).ready(function () {
    const copyBtn = [...document.getElementsByClassName('shorten-link')]
    copyBtn.forEach(btn => btn.addEventListener('click', () => {
    const newUrlLink = btn.getAttribute('data-link')
    navigator.clipboard.writeText(newUrlLink)
    btn.textContent = 'Copied'
  }));


  $("button").click(function () {
    $("button").removeClass("active");
    $(this).addClass("btn btn-outline-dark font-weight-bold");
  });

});
