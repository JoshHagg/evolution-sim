import { useEffect, useRef } from "react";
import * as PIXI from "pixi.js";

const lastPositions = {};

export default function Viewer() {
  const containerRef = useRef(null);

  useEffect(() => {
    if (!containerRef.current) return;

    // Create Pixi app
    const app = new PIXI.Application({
      background: "#111",
      antialias: true,
      resizeTo: containerRef.current,
    });

    containerRef.current.appendChild(app.view);

    // Called every frame to redraw agents
function renderWorld(world) {
  const worldW = 100;
  const worldH = 100;

  const screenW = app.view.width;
  const screenH = app.view.height;

  const scaleX = screenW / worldW;
  const scaleY = screenH / worldH;

  // Use uniform scale so circles stay round
  const scale = Math.min(scaleX, scaleY);

    // calculate centered offsets
  const offsetX = (screenW - worldW * scale) / 2;
  const offsetY = (screenH - worldH * scale) / 2;

  app.stage.removeChildren();

  // Draw food
if (world.food) {
  world.food.forEach(f => {
    const g = new PIXI.Graphics();
    g.beginFill(0xffcc00); // yellow food color

    const sx = offsetX + f.x * scale;
    const sy = offsetY + f.y * scale;

    g.drawCircle(sx, sy, 4);
    g.endFill();

    app.stage.addChild(g);
  });
}

  // Draw agents
  world.agents.forEach(a => {
    // If we have no previous position, initialize it
  if (!lastPositions[a.id]) {
    lastPositions[a.id] = { x: a.x, y: a.y };
  }

  // Previous position
  const prev = lastPositions[a.id];

  // Lerp factor (controls smoothness)
  const lerp = 0.3;

  // Interpolated position
  const ix = prev.x + (a.x - prev.x) * lerp;
  const iy = prev.y + (a.y - prev.y) * lerp;

  // Convert to screen space
  const sx = offsetX + ix * scale;
  const sy = offsetY + iy * scale;

  // Update cache
  lastPositions[a.id] = { x: ix, y: iy };

    const g = new PIXI.Graphics();
    g.beginFill(a.colour);
    g.drawCircle(sx, sy, 6); 
    g.endFill();

    app.stage.addChild(g);
  });
// Draw world border
  const border = new PIXI.Graphics();
border.lineStyle(4, 0xff0000); // red outline

border.drawRect(
    offsetX,
    offsetY,
    worldW * scale,
    worldH * scale
);

app.stage.addChild(border);

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
      style={{ width: "100vw", height: "100vh",margin: 0, padding:0, overflow: "hidden" }}
    />
  );
}
