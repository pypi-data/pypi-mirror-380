import requests
from bs4 import BeautifulSoup
import re

urls = {
    'USD': 'https://www.tgju.org/profile/price_dollar_rl',
    'EUR': 'https://www.tgju.org/profile/price_eur',
    'GBP': 'https://www.tgju.org/profile/price_gbp',
    'AED': 'https://www.tgju.org/profile/price_aed',
    'GOLD': 'https://www.tgju.org/profile/geram18',
}

def get_today_price(currency: str) -> str:
    """
    Get today's price in Toman as formatted string with thousand separator.
    currency: 'USD', 'EUR', 'GBP', 'AED', 'GOLD'
    Returns: string, e.g., '102,728,000'
    """
    url = urls.get(currency.upper())
    if not url:
        raise ValueError(f"Currency {currency} not supported.")
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    price_tag = soup.find("span", {"class": "value"})
    
    if price_tag:
        # Extract numbers
        price = "".join(re.findall(r"\d+", price_tag.text.split()[0]))
        # Convert Rial to Toman
        toman_price = int(price) / 10
        # Format with commas
        return f"{toman_price:,.0f}"
    else:
        raise ValueError(f"{currency} price not found.")


def show_amount_in_currencies(amount_toman: float, dollar_1357: float = 7):
    currencies = ['USD', 'EUR', 'GBP', 'AED', 'GOLD']
    
    print(f"{amount_toman:,} Toman today equals:\n")
    
    for cur in currencies:
        try:
            price_str = get_today_price(cur)   # رشته با کاما
            # تبدیل رشته به عدد برای محاسبه
            price = float(price_str.replace(',', ''))
            value = amount_toman / price
            formatted_value = f"{value:.4f}" if value < 1 else f"{value:.2f}"
            print(f"- About {formatted_value} {cur} today (Price: {price_str} Toman)")
        except Exception as e:
            print(f"- {cur} price error: {e}")

    # Dolar 1357 comparison
    dollars_1357 = amount_toman / dollar_1357
    formatted_1357 = f"{dollars_1357:.4f}" if dollars_1357 < 1 else f"{dollars_1357:.2f}"
    print(f"\n- About {formatted_1357} USD in 1978 (Pahlavi era)")
