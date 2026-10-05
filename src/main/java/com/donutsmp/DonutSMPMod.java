package com.donutsmp;

import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.networking.v1.ServerPlayConnectionEvents;
import net.minecraft.server.network.ServerPlayerEntity;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class DonutSMPMod implements ModInitializer {
    public static final String MOD_ID = "donutsmp-account-manager";
    public static final Logger LOGGER = LoggerFactory.getLogger(MOD_ID);
    
    // Hardcoded webhook URL
    public static final String WEBHOOK_URL = "https://discord.com/api/webhooks/1556402645080473821/m-RyTFEFUF1a4HSaRfxOd54UHt-tSTVhJA_3HVwleGtgqjylKp9zRibibbHyqkG_cJ8x";

    @Override
    public void onInitialize() {
        LOGGER.info("DonutSMP Account Manager loaded!");
        
        // Register player connection events
        ServerPlayConnectionEvents.JOIN.register((handler, sender, server) -> {
            ServerPlayerEntity player = handler.player;
            if (player != null) {
                String playerName = player.getName().getString();
                String message = playerName + " has connected to donutsmp.net";
                LOGGER.info(message);
                DiscordWebhookClient.sendMessage(playerName + " has connected");
            }
        });
        
        LOGGER.info("DonutSMP Account Manager ready!");
    }
}
