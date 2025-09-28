import base64
from io import BytesIO

import anywidget
import matplotlib.pyplot as plt
import numpy as np
import torch
import traitlets


class ImageDebugger:
    @staticmethod
    def tensor_to_numpy(tensor: torch.Tensor) -> np.ndarray:
        """Convert a PyTorch tensor to numpy array for visualization."""
        if tensor.is_cuda:
            tensor = tensor.cpu()
        if tensor.requires_grad:
            tensor = tensor.detach()
        return tensor.numpy()

    @classmethod
    def compare_with_slider(
        cls,
        image1: torch.Tensor | np.ndarray,
        image2: torch.Tensor | np.ndarray,
        titles: tuple[str, str] = ("Image 1", "Image 2"),
        figsize: tuple[int, int] = (10, 5),
    ):
        """Compare two images with an interactive slider using anywidget.

        Args:
            image1, image2: Images to compare
            titles: Titles for both images
            figsize: Figure size
        """
        # Prepare images
        img1 = cls.prepare_for_display(image1)
        img2 = cls.prepare_for_display(image2)

        # Convert images to base64
        def array_to_base64(arr):
            plt.figure(figsize=figsize)
            plt.imshow(arr, cmap="gray" if len(arr.shape) == 2 else None)
            plt.axis("off")

            # Save to base64
            buffer = BytesIO()
            plt.savefig(buffer, format="png", bbox_inches="tight", pad_inches=0)
            plt.close()

            return f"data:image/png;base64,{base64.b64encode(buffer.getvalue()).decode()}"

        # Create widget
        widget = ImageCompareWidget()
        widget.image1_data = array_to_base64(img1)
        widget.image2_data = array_to_base64(img2)
        widget.label1 = titles[0]
        widget.label2 = titles[1]

        return widget

    @classmethod
    def play_video(
        cls,
        frames: torch.Tensor | np.ndarray,
        fps: int = 30,
        figsize: tuple[int, int] = (10, 5),
    ):
        """Create an interactive video player from a batch of frames.

        Args:
            frames: Tensor/array of shape (frames, H, W, C) or (frames, H, W)
            fps: Initial playback speed
            figsize: Figure size for display
        """
        # Convert frames to base64 strings
        frame_data = []
        for frame in frames:
            frame = cls.prepare_for_display(frame)
            frame_data.append(cls._array_to_base64(frame, figsize))

        # Create widget
        widget = VideoPlayerWidget()
        widget.frames = frame_data
        widget.frame_count = len(frame_data)
        widget.fps = fps

        return widget

    @classmethod
    def zoom_image(
        cls,
        image: torch.Tensor | np.ndarray,
        zoom: float = 2.0,
        figsize: tuple[int, int] = (10, 5),
    ):
        """Create an interactive image viewer with magnification lens.

        Args:
            image: Image to view
            zoom: Magnification factor
            figsize: Figure size
        """
        img = cls.prepare_for_display(image)
        img_data = cls._array_to_base64(img, figsize)

        widget = ImageZoomWidget()
        widget.image_data = img_data
        widget.zoom = zoom

        return widget

    @classmethod
    def _array_to_base64(cls, arr: np.ndarray, figsize: tuple[int, int]) -> str:
        """Convert numpy array to base64 string."""
        plt.figure(figsize=figsize)
        plt.imshow(arr, cmap="gray" if len(arr.shape) == 2 else None)
        plt.axis("off")

        buffer = BytesIO()
        plt.savefig(buffer, format="png", bbox_inches="tight", pad_inches=0)
        plt.close()

        return f"data:image/png;base64,{base64.b64encode(buffer.getvalue()).decode()}"

    @classmethod
    def compare_with_slider_pywidget(
        cls,
        image1: torch.Tensor | np.ndarray,
        image2: torch.Tensor | np.ndarray,
        titles: tuple[str, str] = ("Image 1", "Image 2"),
        figsize: tuple[int, int] = (10, 5),
    ):
        """Compare two images with an interactive slider.

        Args:
            image1, image2: Images to compare
            titles: Titles for both images
            figsize: Figure size
        """
        import ipywidgets as widgets
        from ipywidgets import interactive

        # Prepare images
        img1 = cls.prepare_for_display(image1)
        img2 = cls.prepare_for_display(image2)

        def view_images(position):
            fig, ax = plt.subplots(figsize=figsize)
            ax.imshow(img1, cmap="gray" if len(img1.shape) == 2 else None)

            # Create a masked version of image2 to show only part of it
            height = img2.shape[0]
            mask = np.zeros_like(img2, dtype=bool)
            mask[:, : int(position * img2.shape[1])] = True

            # Show image2 only where mask is True
            masked_img = np.where(mask, img2, img1)
            ax.imshow(masked_img, cmap="gray" if len(img2.shape) == 2 else None)

            # Add a line at the split
            ax.axvline(x=position * img2.shape[1], color="r", linewidth=2)

            ax.set_title(f"{titles[0]} | {titles[1]}")
            plt.axis("off")
            plt.show()

        return interactive(
            view_images,
            position=widgets.FloatSlider(min=0, max=1, step=0.01, value=0.5),
        )

    @classmethod
    def overlay_mask(
        cls,
        image: torch.Tensor | np.ndarray,
        mask: torch.Tensor | np.ndarray,
        color: str | tuple[float, float, float] = "red",
        alpha: float = 0.5,
        figsize: tuple[int, int] = (10, 5),
    ):
        """Overlay a mask on an image with specified color and opacity.

        Args:
            image: Base image
            mask: Binary mask to overlay
            color: Color for the overlay (name or RGB tuple)
            alpha: Opacity of the overlay (0-1)
            figsize: Figure size
        """
        # Prepare image and mask
        img = cls.prepare_for_display(image)
        msk = cls.prepare_for_display(mask)

        # Convert color to RGB if it's a string
        if isinstance(color, str):
            from matplotlib.colors import to_rgb

            color = to_rgb(color)

        # Create colored mask
        colored_mask = np.zeros((*msk.shape, 3) if len(msk.shape) == 2 else msk.shape[:-1] + (3,))
        for i in range(3):
            colored_mask[..., i] = msk * color[i]

        # Convert image to RGB if needed
        if len(img.shape) == 2:
            img = np.stack([img] * 3, axis=-1)

        # Blend images
        blended = (1 - alpha) * img + alpha * colored_mask

        plt.figure(figsize=figsize)
        plt.imshow(np.clip(blended, 0, 1))
        plt.axis("off")
        plt.show()

    @classmethod
    def create_gif(
        cls,
        frames: torch.Tensor | np.ndarray,
        output_path: str = "animation.gif",
        duration: int = 100,
        loop: int = 0,
        figsize: tuple[int, int] = (10, 5),
    ):
        """Create a GIF from a batch of frames.

        Args:
            frames: Tensor of shape (frames, H, W) or (frames, H, W, C)
            output_path: Path to save the GIF
            duration: Duration for each frame in milliseconds
            loop: Number of times to loop (0 = infinite)
            figsize: Figure size for each frame
        """
        import imageio

        # Prepare frames
        if isinstance(frames, torch.Tensor):
            frames = cls.tensor_to_numpy(frames)

        # Normalize each frame
        normalized_frames = [cls.prepare_for_display(frame) for frame in frames]

        # Save as GIF
        imageio.mimsave(output_path, normalized_frames, duration=duration / 1000, loop=loop)

        # Display the GIF
        from IPython.display import Image, display

        display(Image(output_path))

    @classmethod
    def side_by_side_comparison(
        cls,
        images: list[torch.Tensor | np.ndarray],
        titles: list[str],
        figsize: tuple[int, int] = (15, 5),
        share_axes: bool = True,
    ):
        """Display images side by side with synchronized zoom/pan.

        Args:
            images: List of images to compare
            titles: List of titles for each image
            figsize: Figure size
            share_axes: Whether to synchronize zoom/pan across images
        """
        n_images = len(images)
        fig, axes = plt.subplots(1, n_images, figsize=figsize, sharex=share_axes, sharey=share_axes)
        if n_images == 1:
            axes = [axes]

        for ax, img, title in zip(axes, images, titles, strict=False):
            img_display = cls.prepare_for_display(img)
            ax.imshow(
                img_display,
                cmap="gray" if len(img_display.shape) == 2 else None,
            )
            ax.set_title(title)
            ax.axis("off")

        plt.tight_layout()
        plt.show()

    @classmethod
    def highlight_differences(
        cls,
        image1: torch.Tensor | np.ndarray,
        image2: torch.Tensor | np.ndarray,
        threshold: float = 0.1,
        color: str = "red",
        figsize: tuple[int, int] = (15, 5),
    ):
        """Show differences between two images by highlighting them.

        Args:
            image1, image2: Images to compare
            threshold: Difference threshold to highlight
            color: Color for highlighting differences
            figsize: Figure size
        """
        img1 = cls.prepare_for_display(image1)
        img2 = cls.prepare_for_display(image2)

        diff = np.abs(img1 - img2) > threshold

        plt.figure(figsize=figsize)
        plt.subplot(131)
        plt.imshow(img1, cmap="gray" if len(img1.shape) == 2 else None)
        plt.title("Image 1")
        plt.axis("off")

        plt.subplot(132)
        plt.imshow(img2, cmap="gray" if len(img2.shape) == 2 else None)
        plt.title("Image 2")
        plt.axis("off")

        plt.subplot(133)
        plt.imshow(img1, cmap="gray" if len(img1.shape) == 2 else None)
        plt.imshow(diff, cmap="binary", alpha=0.5)
        plt.title("Differences")
        plt.axis("off")

        plt.tight_layout()
        plt.show()

    @staticmethod
    def normalize_image(img: np.ndarray) -> np.ndarray:
        """Normalize image to 0-1 range."""
        if img.max() - img.min() > 0:
            return (img - img.min()) / (img.max() - img.min())
        return img

    @staticmethod
    def prepare_for_display(
        img: torch.Tensor | np.ndarray,
    ) -> np.ndarray:
        """Prepare image/mask for display by converting to correct shape and format.

        Args:
            img: Input image or mask (torch.Tensor or np.ndarray)

        Returns
        -------
            np.ndarray: Image ready for display (H, W) or (H, W, C)
        """
        # Convert to numpy if tensor
        if isinstance(img, torch.Tensor):
            img = ImageDebugger.tensor_to_numpy(img)

        # Handle different shapes
        if len(img.shape) == 4:  # (B, C, H, W) or (B, H, W, C)
            img = img[0]  # Take first batch

        if len(img.shape) == 3:
            # Handle (C, H, W) format
            if img.shape[0] in [1, 3, 4]:  # Channels first
                img = np.transpose(img, (1, 2, 0))

            # Squeeze single channels
            if img.shape[-1] == 1:
                img = np.squeeze(img, axis=-1)

        # Ensure float
        if img.dtype != np.float32:
            img = img.astype(np.float32)

        return ImageDebugger.normalize_image(img)

    @classmethod
    def show_image_grid(
        cls,
        images: list[torch.Tensor | np.ndarray],
        titles: list[str],
        cmaps: list[str] | None = None,
        figsize: tuple[int, int] = (15, 5),
        colorbar: bool = True,
    ):
        """Display a grid of images with titles and optional colorbars.

        Args:
            images: List of images (torch tensors or numpy arrays)
            titles: List of titles for each image
            cmaps: List of colormaps for each image (default: None, will use 'gray' for 1-channel, 'viridis' for others)
            figsize: Figure size (width, height)
            colorbar: Whether to show colorbar
        """
        n_images = len(images)
        fig, axes = plt.subplots(1, n_images, figsize=figsize)
        if n_images == 1:
            axes = [axes]

        prepared_images = [cls.prepare_for_display(img) for img in images]

        if cmaps is None:
            cmaps = [
                "gray" if img.shape[-1] == 1 or len(img.shape) == 2 else None  # "viridis"
                for img in prepared_images
            ]

        for ax, img, title, cmap in zip(axes, prepared_images, titles, cmaps, strict=False):
            # Convert to numpy if tensor
            if isinstance(img, torch.Tensor):
                img = cls.tensor_to_numpy(img)

            # Squeeze single-channel images
            if len(img.shape) == 3 and img.shape[-1] == 1:
                img = img.squeeze(-1)

            # Display image
            im = ax.imshow(cls.normalize_image(img), cmap=cmap)
            ax.set_title(title)
            ax.axis("off")
            if colorbar:
                plt.colorbar(im, ax=ax)

        plt.tight_layout()
        plt.show()

    @classmethod
    def compare_operations(
        cls,
        original: torch.Tensor,
        results: list[torch.Tensor],
        operation_names: list[str],
        figsize: tuple[int, int] = (20, 4),
    ):
        """Compare original image with multiple operation results.

        Args:
            original: Original image/mask
            results: List of resulting images/masks from different operations
            operation_names: Names of the operations for titles
            figsize: Figure size
        """
        all_images = [original] + results
        all_titles = ["Original"] + operation_names
        cls.show_image_grid(all_images, all_titles, figsize=figsize)

    @classmethod
    def show_trimap_components(
        cls,
        mask: torch.Tensor,
        trimap: torch.Tensor,
        eroded: torch.Tensor | None = None,
        dilated: torch.Tensor | None = None,
        figsize: tuple[int, int] = (20, 4),
    ):
        """Visualize trimap components for debugging.

        Args:
            mask: Original mask
            trimap: Generated trimap
            eroded: Eroded mask (optional)
            dilated: Dilated mask (optional)
            figsize: Figure size
        """
        images = [mask, trimap]
        titles = ["Original Mask", "Trimap"]

        if eroded is not None:
            images.append(eroded)
            titles.append("Eroded (Core)")

        if dilated is not None:
            images.append(dilated)
            titles.append("Dilated (Boundary)")

        cls.show_image_grid(images, titles, figsize=figsize)

    @classmethod
    def show_trimap_values(cls, trimap: torch.Tensor):
        """Display unique values in trimap for verification."""
        if isinstance(trimap, torch.Tensor):
            trimap = cls.tensor_to_numpy(trimap)
        unique_values = np.unique(trimap)
        print(f"Unique values in trimap: {unique_values}")


class VideoPlayerWidget(anywidget.AnyWidget):
    _esm = """
    function render({ model, el }) {
        const container = document.createElement('div');
        container.style.position = 'relative';

        // Create video controls
        const controls = document.createElement('div');
        controls.style.display = 'flex';
        controls.style.alignItems = 'center';
        controls.style.gap = '10px';
        controls.style.marginBottom = '10px';

        // Play/Pause button
        const playBtn = document.createElement('button');
        playBtn.innerHTML = '⏵';
        playBtn.style.width = '40px';

        // Slider
        const slider = document.createElement('input');
        slider.type = 'range';
        slider.min = '0';
        slider.max = model.get('frame_count') - 1;
        slider.value = '0';
        slider.style.flex = '1';

        // Frame counter
        const counter = document.createElement('span');
        counter.textContent = `1/${model.get('frame_count')}`;

        // FPS control
        const fpsInput = document.createElement('input');
        fpsInput.type = 'number';
        fpsInput.min = '1';
        fpsInput.max = '60';
        fpsInput.value = model.get('fps');
        fpsInput.style.width = '60px';

        // Image display
        const img = document.createElement('img');
        img.style.width = '100%';
        img.src = model.get('frames')[0];

        let isPlaying = false;
        let intervalId = null;

        const updateFrame = (index) => {
            img.src = model.get('frames')[index];
            counter.textContent = `${index + 1}/${model.get('frame_count')}`;
            slider.value = index;
            model.set('current_frame', index);
            model.save_changes();
        };

        const togglePlay = () => {
            isPlaying = !isPlaying;
            playBtn.innerHTML = isPlaying ? '⏸' : '⏵';

            if (isPlaying) {
                intervalId = setInterval(() => {
                    let nextFrame = (parseInt(slider.value) + 1) % model.get('frame_count');
                    updateFrame(nextFrame);
                }, 1000 / model.get('fps'));
            } else {
                clearInterval(intervalId);
            }
        };

        playBtn.addEventListener('click', togglePlay);
        slider.addEventListener('input', (e) => {
            updateFrame(parseInt(e.target.value));
            if (isPlaying) togglePlay();
        });

        fpsInput.addEventListener('change', (e) => {
            model.set('fps', parseInt(e.target.value));
            model.save_changes();
            if (isPlaying) {
                clearInterval(intervalId);
                togglePlay();
            }
        });

        controls.appendChild(playBtn);
        controls.appendChild(slider);
        controls.appendChild(counter);
        controls.appendChild(fpsInput);

        container.appendChild(controls);
        container.appendChild(img);
        el.appendChild(container);
    }
    export default { render };
    """

    frames = traitlets.List([]).tag(sync=True)
    frame_count = traitlets.Int(0).tag(sync=True)
    current_frame = traitlets.Int(0).tag(sync=True)
    fps = traitlets.Int(30).tag(sync=True)


class ImageZoomWidget(anywidget.AnyWidget):
    _esm = """
    function render({ model, el }) {
        const container = document.createElement('div');
        container.style.position = 'relative';
        container.style.width = '100%';

        // Main image
        const img = document.createElement('img');
        img.src = model.get('image_data');
        img.style.width = '100%';

        // Magnifier
        const magnifier = document.createElement('div');
        magnifier.style.position = 'absolute';
        magnifier.style.border = '2px solid white';
        magnifier.style.borderRadius = '50%';
        magnifier.style.width = '150px';
        magnifier.style.height = '150px';
        magnifier.style.boxShadow = '0 0 10px rgba(0,0,0,0.5)';
        magnifier.style.display = 'none';
        magnifier.style.backgroundImage = `url(${model.get('image_data')})`;
        magnifier.style.backgroundRepeat = 'no-repeat';
        magnifier.style.pointerEvents = 'none';

        const zoom = model.get('zoom');

        img.addEventListener('mousemove', (e) => {
            const rect = img.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            magnifier.style.left = `${x - 75}px`;
            magnifier.style.top = `${y - 75}px`;

            const bgX = x * zoom;
            const bgY = y * zoom;
            magnifier.style.backgroundPosition = `-${bgX - 75}px -${bgY - 75}px`;
            magnifier.style.backgroundSize = `${img.width * zoom}px`;
        });

        img.addEventListener('mouseenter', () => {
            magnifier.style.display = 'block';
        });

        img.addEventListener('mouseleave', () => {
            magnifier.style.display = 'none';
        });

        container.appendChild(img);
        container.appendChild(magnifier);
        el.appendChild(container);
    }
    export default { render };
    """

    image_data = traitlets.Unicode("").tag(sync=True)
    zoom = traitlets.Float(2.0).tag(sync=True)


class ImageCompareWidget(anywidget.AnyWidget):
    _esm = """
    function render({ model, el }) {
        // Create container
        const container = document.createElement('div');
        container.style.position = 'relative';
        container.style.width = '100%';
        container.style.maxWidth = '800px';

        // Create images
        const img1 = document.createElement('img');
        img1.src = model.get("image1_data");
        img1.style.width = '100%';
        img1.style.display = 'block';

        const img2 = document.createElement('img');
        img2.src = model.get("image2_data");
        img2.style.width = '100%';
        img2.style.position = 'absolute';
        img2.style.top = '0';
        img2.style.left = '0';
        img2.style.clipPath = `polygon(0 0, ${model.get("position")}% 0, ${model.get("position")}% 100%, 0 100%)`;

        // Create slider line
        const line = document.createElement('div');
        line.style.position = 'absolute';
        line.style.top = '0';
        line.style.bottom = '0';
        line.style.width = '2px';
        line.style.backgroundColor = 'white';
        line.style.left = `${model.get("position")}%`;
        line.style.cursor = 'ew-resize';
        line.style.boxShadow = '0 0 5px rgba(0,0,0,0.5)';

        // Create labels
        const label1 = document.createElement('div');
        label1.textContent = model.get("label1");
        label1.style.position = 'absolute';
        label1.style.top = '10px';
        label1.style.left = '10px';
        label1.style.color = 'white';
        label1.style.textShadow = '0 0 3px black';
        label1.style.fontSize = '14px';

        const label2 = document.createElement('div');
        label2.textContent = model.get("label2");
        label2.style.position = 'absolute';
        label2.style.top = '10px';
        label2.style.right = '10px';
        label2.style.color = 'white';
        label2.style.textShadow = '0 0 3px black';
        label2.style.fontSize = '14px';

        // Add drag functionality
        let isDragging = false;

        const handleDrag = (e) => {
            if (!isDragging) return;

            const rect = container.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const pos = Math.max(0, Math.min(100, (x / rect.width) * 100));

            model.set("position", pos);
            model.save_changes();
        };

        container.addEventListener('mousedown', () => isDragging = true);
        document.addEventListener('mousemove', handleDrag);
        document.addEventListener('mouseup', () => isDragging = false);

        // Update on model change
        model.on("change:position", () => {
            const pos = model.get("position");
            img2.style.clipPath = `polygon(0 0, ${pos}% 0, ${pos}% 100%, 0 100%)`;
            line.style.left = `${pos}%`;
        });

        // Append elements
        container.appendChild(img1);
        container.appendChild(img2);
        container.appendChild(line);
        container.appendChild(label1);
        container.appendChild(label2);
        el.appendChild(container);
    }
    export default { render };
    """

    _css = """
    """

    position = traitlets.Float(50.0).tag(sync=True)
    image1_data = traitlets.Unicode("").tag(sync=True)
    image2_data = traitlets.Unicode("").tag(sync=True)
    label1 = traitlets.Unicode("Image 1").tag(sync=True)
    label2 = traitlets.Unicode("Image 2").tag(sync=True)
