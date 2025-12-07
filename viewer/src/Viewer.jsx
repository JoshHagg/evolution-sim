import { useEffect, useRef } from "react";
import * as PIXI from "pixi.js";

export default function Viewer() {
  const containerRef = useRef(null);

  useEffect(() => {
    // Create Pixi app
    const app = new PIXI.Application({
      background: "#111",
      antialias: true,
      resizeTo: window,
    });

    containerRef.current.appendChild(app.view);

    // Called every frame to redraw agents
function renderWorld(world) {
  const worldW = 100;
  const worldH = 100;

  const screenW = app.renderer.width;
  const screenH = app.renderer.height;

  const scaleX = screenW / worldW;
  const scaleY = screenH / worldH;

  // Use uniform scale so circles stay round
  const scale = Math.min(scaleX, scaleY);

  app.stage.removeChildren();

  // Draw agents
  world.agents.forEach(a => {
    const g = new PIXI.Graphics();
    g.beginFill(0x00ff00);

    // Scale world → screen
    const sx = a.x * scale;
    const sy = a.y * scale;

    g.drawCircle(sx, sy, 4 * scale); 
    g.endFill();

    app.stage.addChild(g);
  });
}


    // Fetch loop
    async function updateLoop() {
      try {
        const res = await fetch("http://127.0.0.1:8000/world");
        const data = await res.json();

        renderWorld(data);
      } catch (err) {
        console.error("World fetch failed:", err);
      }

      requestAnimationFrame(updateLoop);
    }

    updateLoop();

    return () => app.destroy(true);
  }, []);

  return (
    <div
      ref={containerRef}
      style={{ width: "100%", height: "100%", overflow: "hidden" }}
    />
  );
}
