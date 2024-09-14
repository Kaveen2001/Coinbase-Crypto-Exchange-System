// Sample market data
const sampleMarketData = {
  "BTC": {"price": "50000", "volume": "1500"},
  "ETH": {"price": "4000", "volume": "10000"},
  "LTC": {"price": "200", "volume": "5000"},
  "XRP": {"price": "1.2", "volume": "2000000"},
  "ADA": {"price": "2.5", "volume": "3000000"},
  "DOGE": {"price": "0.3", "volume": "15000000"},
  "DOT": {"price": "35", "volume": "800000"},
  "BCH": {"price": "700", "volume": "12000"},
  "LINK": {"price": "30", "volume": "250000"},
  "XLM": {"price": "0.4", "volume": "10000000"}
};

// Fetch market data and populate the table
function fetchMarketData() {
  const marketDataBody = document.getElementById('market-data-body');
  marketDataBody.innerHTML = ''; // Clear existing data

  for (const crypto in sampleMarketData) {
      const row = `
          <tr>
              <td>${crypto}</td>
              <td>$${sampleMarketData[crypto].price}</td>
              <td>${sampleMarketData[crypto].volume}</td>
          </tr>
      `;
      marketDataBody.innerHTML += row;
  }
}

// Handle trade form submission
document.getElementById('trade-form').addEventListener('submit', function(e) {
  e.preventDefault();

  const crypto = document.getElementById('crypto').value;
  const action = document.getElementById('action').value;
  const amount = document.getElementById('amount').value;

  // Execute trade via API (mocked)
  fetch('/api/trade', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({ crypto, action, amount })
  })
  .then(response => response.json())
  .then(data => {
      // Update the status message
      const statusMessage = document.getElementById('status-message');
      if (data.message === "Trade executed successfully!") {
          statusMessage.className = 'status-message success';
          statusMessage.innerHTML = `Trade executed successfully: ${action.toUpperCase()} ${amount} ${crypto}`;
          fetchMarketData(); // Optionally update the market data after a trade
      } else {
          statusMessage.className = 'status-message error';
          statusMessage.innerHTML = `Trade failed: ${data.message}`;
      }
      statusMessage.style.display = 'block'; // Show the status message
  })
  .catch(error => {
      // Handle errors
      const statusMessage = document.getElementById('status-message');
      statusMessage.className = 'status-message error';
      statusMessage.innerHTML = `Trade failed: ${error.message}`;
      statusMessage.style.display = 'block';
  });
});

// Fetch market data on page load
fetchMarketData();
