const std = @import("std");

pub fn main() !void {
    // read lines from stdin into an array
    var lines = try std.io.getStdIn().readLinesAlloc(std.heap.page_allocator);
    defer std.heap.page_allocator.free(lines);

    // now print each line to stderr
    for (lines) |line| {
        try std.io.getStdErr().print("{}\n", .{line});
    }
}
