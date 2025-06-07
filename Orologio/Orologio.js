const $ = (selector) => {
    return document.querySelector(selector);
}
const hour = $('.hour');
const dot = $('.dot');
const min = $('.min');
const sec = $('.sec');
const week = $('.week');
let showDot = true;

function update() {
    showDot = !showDot;
    const now = new Date();

    if (showDot) {
        dot.classList.add('invsible');
    } else {
        dot.classList.remove('invsible');
    }    
    hour.textContent = String(now.getHours())
        .padStart(2, '0');
    min.textContent = String(now.getMinutes())
        .padStart(2, '0');
    sec.textContent = String(now.getSeconds())
        .padStart(2, '0');

    Array
        .from(week.children)
        .forEach(
            (ele) => {
                ele.clas
            }
        );
    week
        .children[now.getDay()]
        .classList
        .add('active');
};

setInterval(update, 500)