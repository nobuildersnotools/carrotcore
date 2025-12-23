CarrotCore — Custom Worldgen Datapack for carrot-craft.org

Lightweight worldgen adjustments that improve play experience for legacy Minecraft clients (1.8–1.12) connecting to modern servers via ViaVersion. CarrotCore clamps terrain to y=0–255 and recreates a classic pre-Caves & Cliffs feel while keeping modern structures and biomes intact.

<img width="1919" height="1125" alt="Screenshot from 2025-11-24 14-52-03" src="https://github.com/user-attachments/assets/a23a48d7-51e4-4d9b-af9d-d8038aa2cee0" />


**Overview:**

- Designed for servers with mixed-version players; makes worlds behave like older clients expect without removing modern content.
- Non-destructive: preserves structures and biomes added by modern server versions.
- Tested on Minecraft `1.21.1`.

**Key Features:**

- Terrain height clamped to `y=0-255` for legacy client compatibility.
- Worldgen resembles classic terrain (pre-1.18) while still supporting modern features.
- Minimal, focused datapack — intended to be layered on top of an existing server worldgen.

**Supported Versions:**

- Server: any modern server supporting datapacks (recommended `1.21.1+`).
- Clients: legacy clients such as `1.8`–`1.12` using ViaVersion to connect.

**Requirements:**

- `Retro Caves` datapack (required): https://modrinth.com/datapack/retro-caves — CarrotCore relies on Retro Caves for correct cave generation and vertical behavior.
- ViaVersion (or similar) if you want legacy clients to connect to a modern server.

**Installation (server owner):**

1. Download CarrotCore and the `Retro Caves` datapack.
2. Place datapack zip folders in your world `datapacks/` directory.
3. Recommended order: install `Retro Caves` first, then `CarrotCore`.
4. Restart the server (or run `/reload` during maintenance) and verify the datapacks are enabled with `/datapack list`.

**Usage Notes:**

- New chunks will use the adjusted worldgen; existing chunks remain unchanged unless regenerated or forced with external tools.
- If you use world-editing / region tools to regenerate areas, ensure `Retro Caves` and `CarrotCore` are active during regeneration.

**Compatibility & Limitations:**

- This datapack clamps world heights to `y=0-255`; it does not modify player/client rendering beyond that.
- Some server-side features introduced in newer snapshots may behave differently for very old clients — test on a staging server before deploying to production.

**Credits & Inspiration:**

- Based on ideas and code from No Generation Y: https://modrinth.com/datapack/no-generation-y
- Uses patterns from No More Copper Ore: https://modrinth.com/datapack/no-more-copper-ore

**Contributing:**

- Pull requests welcome. Open issues or PRs at: [your-repo-link] (replace with your GitHub or Modrinth repository URL).
- When submitting PRs, include Minecraft version tested and brief reproduction steps for changes.
**Changelog (initial):**

- 0.1 — Initial release: world height clamp, classic-style terrain, Retro Caves integration.

If you'd like, I can also: add an example `pack.mcmeta`, generate a `modrinth` or `curseforge` friendly README, or create an installation script. Tell me which next step you prefer.
