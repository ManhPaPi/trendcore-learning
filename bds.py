import requests
from bs4 import BeautifulSoup

# URL trang cần cào
url = "https://batdongsan.com.vn/nha-ban/quan-hai-ba-trung"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

listings = soup.select(".re__card")

for index, listing in enumerate(listings, start=1):
    try:
        # Tiêu đề
        title = listing.select_one(".re__card-title").text.strip() if listing.select_one(".re__card-title") else "N/A"

        # Giá
        price = listing.select_one(".re__card-config-price").text.strip() if listing.select_one(".re__card-config-price") else "N/A"

        # Diện tích
        area = listing.select_one(".re__card-config-area").text.strip() if listing.select_one(".re__card-config-area") else "N/A"

        # Giá/m2
        price_per_m2 = listing.select_one(".re__card-config-pricePerSquareMeter").text.strip() if listing.select_one(".re__card-config-pricePerSquareMeter") else "N/A"

        # Số phòng ngủ
        bedrooms = listing.select_one(".re__card-config-bedroom").text.strip() if listing.select_one(".re__card-config-bedroom") else "N/A"

        # Số WC
        bathrooms = listing.select_one(".re__card-config-toilet").text.strip() if listing.select_one(".re__card-config-toilet") else "N/A"

        # Vị trí
        address = listing.select_one(".re__card-address").text.strip() if listing.select_one(".re__card-address") else "N/A"

        # Người đăng
        poster = listing.select_one(".re__card-contact-name").text.strip() if listing.select_one(".re__card-contact-name") else "N/A"

        # Liên hệ
        phone = listing.select_one(".re__card-contact-phone").text.strip() if listing.select_one(".re__card-contact-phone") else "N/A"

        # In kết quả theo mẫu yêu cầu
        print(f"--- Tin số {index} ---")
        print(f"Tiêu đề: {title}")
        print(f"Giá: {price}")
        print(f"Diện tích: {area}")
        print(f"Giá/m²: {price_per_m2}")
        print(f"Phòng ngủ: {bedrooms}")
        print(f"WC: {bathrooms}")
        print(f"Vị trí: {address}")
        print(f"Người đăng: {poster}")
        print(f"Liên hệ: {phone}")
        print("-" * 80)

    except Exception as e:
        print(f"Lỗi ở tin thứ {index}: {e}")
        