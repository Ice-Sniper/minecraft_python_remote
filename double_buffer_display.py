# from mcpi2.vec3 import Vec3
# import param_MCJAVA as param

from mcpi.vec3 import Vec3
import param_MCPI as param

from font_5x7 import font_design, FONT_WIDTH, FONT_HEIGHT


# display frame
DISP_HEIGHT = FONT_HEIGHT + 4
BLOCK_FRAME = param.GOLD_BLOCK


class BufferDisplay():
    """
    Double-buffer display for voxel letters in Minecraft.
    To improve performance, only changes are rendered.
    """

    def __init__(self, anchor_position=Vec3(0,60,0)):
        """
        Set everything up to render messages into the world
        at the given position.
        """
        self.last_message = ''
        self.offscreen = []
        self.onscreen = []
        self.anchor_position = anchor_position

    def render(self, message, blockId=param.GOLD_BLOCK):
        """
        Put the message into the off-screen buffer.
        """
        if message != self.last_message:  # Do nothing if the message has not changed.
            self.last_message = message   # Save for the next time.

            self.offscreen = []  # Clear any previous use of the buffer.
            letter_offset = 0
            for letter in message:
                rendition = font_design[letter]
                line_offset = 0
                for line in rendition:
                    if len(self.offscreen) <= line_offset:
                        # Make space to store the drawing.
                        self.offscreen.append([])
                    dot_offset = 0
                    for dot in line:
                        if dot == '0':  # on
                            self.offscreen[line_offset] \
                                .append(blockId)
                        else:           # off
                            self.offscreen[line_offset].append(param.AIR)
                        dot_offset += 1
                    for _blank in range(dot_offset, FONT_WIDTH + 1):
                        # Expand short lines to the full width.
                        self.offscreen[line_offset].append(param.AIR)
                    line_offset += 1
                letter_offset += 1

            # Clear the onscreen buffer at the beginning.
            if self.onscreen == []:
                # No onscreen copy - so make it the same size as the offscreen image.
                # Fill with AIR voxels.
                line_offset = 0
                for line in self.offscreen:
                    self.onscreen.append([])
                    for dot in line:
                        self.onscreen[line_offset].append(param.AIR)
                    line_offset += 1

    def flip(self, mc):
        """
        Put the off-screen buffer onto the screen.
        Only send the differences.
        Remember the new screen for next flip as on-screen.
        """
        line_offset = 0
        for line in self.offscreen:
            dot_offset = 0
            for dot in line:
                # if space do nothing
                if self.onscreen[line_offset][dot_offset] != dot:
                    self.onscreen[line_offset][dot_offset] = dot
                    mc.setBlock(self.anchor_position.x + 2 + dot_offset,
                                self.anchor_position.y - 2 - line_offset,
                                self.anchor_position.z,
                                dot)
                dot_offset += 1
            line_offset += 1

    def clear(self, mc, num_of_digits, block_frame=BLOCK_FRAME):
        x, y, z = self.anchor_position  # topleft of the display frame
        x1 = x + (FONT_WIDTH + 1) * num_of_digits + 2
        y1 = y - DISP_HEIGHT + 1
        mc.setBlocks(x,     y,     z,    x1,     y1,     z,  block_frame)
        mc.setBlocks(x + 1, y - 1, z,    x1 - 1, y1 + 1, z,  param.AIR)
