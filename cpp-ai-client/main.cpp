#include <iostream>
#include <string>
#include <curl/curl.h>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

// Callback za curl - skuplja HTTP response
static size_t WriteCallback(void* contents, size_t size, size_t nmemb, std::string* output) {
    output->append((char*)contents, size * nmemb);
    return size * nmemb;
}

std::string pitaj_ai(const std::string& pitanje) {
    CURL* curl = curl_easy_init();
    std::string response;

    if (!curl) {
        return "Greška: ne mogu da inicijalizujem curl";
    }

    // Napravi JSON body
    json body = {
        {"model", "local-llama"},
        {"messages", json::array({
            {{"role", "user"}, {"content", pitanje}}
        })}
    };
    std::string body_str = body.dump();

    // Podesi curl
    curl_easy_setopt(curl, CURLOPT_URL, "http://localhost:4000/v1/chat/completions");
    curl_easy_setopt(curl, CURLOPT_POSTFIELDS, body_str.c_str());
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, &response);

    // Headers
    struct curl_slist* headers = nullptr;
    headers = curl_slist_append(headers, "Content-Type: application/json");
    headers = curl_slist_append(headers, "Authorization: Bearer sk-mojkljuc123");
    curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);

    // Izvrši request
    CURLcode res = curl_easy_perform(curl);
    curl_slist_free_all(headers);
    curl_easy_cleanup(curl);

    if (res != CURLE_OK) {
        return "Greška: " + std::string(curl_easy_strerror(res));
    }

    // Parsiraj JSON odgovor
    try {
        json parsed = json::parse(response);
        return parsed["choices"][0]["message"]["content"];
    } catch (...) {
        return "Greška parsiranja: " + response;
    }
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cout << "Korišćenje: ai-client \"tvoje pitanje\"" << std::endl;
        return 1;
    }

    std::string pitanje = argv[1];
    std::cout << "Pitanje: " << pitanje << std::endl;
    std::cout << "Odgovor: " << pitaj_ai(pitanje) << std::endl;

    return 0;
}