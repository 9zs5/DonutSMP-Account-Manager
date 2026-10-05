package com.donutsmp;

import com.google.gson.Gson;
import com.google.gson.JsonObject;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class DiscordWebhookClient {
    private static final HttpClient HTTP_CLIENT = HttpClient.newHttpClient();
    private static final Gson GSON = new Gson();
    
    /**
     * Send a message to Discord via webhook
     * No authentication required - uses hardcoded webhook URL
     */
    public static void sendMessage(String message) {
        try {
            JsonObject json = new JsonObject();
            json.addProperty("content", message);
            
            String jsonString = GSON.toJson(json);
            
            HttpRequest request = HttpRequest.newBuilder()
                    .uri(new URI(DonutSMPMod.WEBHOOK_URL))
                    .header("Content-Type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(jsonString))
                    .build();
            
            HTTP_CLIENT.sendAsync(request, HttpResponse.BodyHandlers.discarding());
        } catch (Exception e) {
            DonutSMPMod.LOGGER.error("[DonutSMP] Failed to send Discord message", e);
        }
    }
}