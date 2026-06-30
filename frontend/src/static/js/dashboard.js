// ===== Chart =====

if (typeof cardsData !== "undefined" && cardsData.length) {
    const bankCounts = {};
    cardsData.forEach(card => {
        bankCounts[card.bank] = (bankCounts[card.bank] || 0) + 1;
    });

    new Chart(document.getElementById("bankChart"), {
        type: "bar",
        data: {
            labels: Object.keys(bankCounts),
            datasets: [{
                label: "Number of Cards",
                data: Object.values(bankCounts),
                backgroundColor: "#2563eb",
                borderRadius: 6,
            }]
        },
        options: {
            responsive: true,
            plugins: { legend: { display: false } },
            scales: { y: { beginAtZero: true, ticks: { stepSize: 1 } } }
        }
    });
}

// ===== Search + bank filter =====

const search = document.getElementById("search");
const bankFilter = document.getElementById("bankFilter");

function filterCards() {
    const keyword = search.value.toLowerCase();
    const bank = bankFilter ? bankFilter.value : "";

    document.querySelectorAll(".card").forEach(card => {
        const text = card.innerText.toLowerCase();
        const cardBank = card.dataset.bank;
        const matchesSearch = text.includes(keyword);
        const matchesBank = !bank || cardBank === bank;
        card.style.display = (matchesSearch && matchesBank) ? "block" : "none";
    });
}

search.addEventListener("input", filterCards);
if (bankFilter) {
    bankFilter.addEventListener("change", filterCards);
}

// ===== View details navigation =====

document.querySelectorAll(".view-btn").forEach(btn => {
    btn.addEventListener("click", () => {
        window.location.href = `/dashboard/${encodeURIComponent(btn.dataset.title)}`;
    });
});