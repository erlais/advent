lower = Set(Char.('a':'z'))
upper = Set(Char.('A':'Z'))

get_adjacent(y, x) = [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]
is_tunnel(y, x) = in(grid[y][x], ('.', '@'))
is_key(y, x) = in(grid[y][x], lower)
is_door(y, x) = in(grid[y][x], upper)

lines = readlines("input18")
grid = [[char for char in l] for l=lines]

all_keys = Dict()
start_pos = nothing

for (y, row) in enumerate(grid)
    for (x, col) in enumerate(row)
        global all_keys, start_pos
        loc = grid[y][x]
        if loc in lower
            all_keys[loc] = (y, x)
        elseif loc == '@'
            start_pos = (y, x)
        end
    end
end

status = (start_pos[1], start_pos[2], [], 0)
Q = [status]
seen = Set()

while length(Q) > 0
    global Q, seen
    pos = popfirst!(Q)
    if Set(pos[3]) == Set(keys(all_keys))
        println("Found all keys in $(pos[4]) moves!")
        Q = []
        break
    end
    pos[1:3] in seen ? continue : nothing
    push!(seen, pos[1:3])
    adj = get_adjacent(pos[1], pos[2])
    for (py, px) in adj

        if is_tunnel(py, px)
            push!(Q, (py, px, pos[3], pos[4] + 1))

        elseif is_key(py, px)
            found_key = grid[py][px]
            if found_key in pos[3]
                push!(Q, (py, px, pos[3], pos[4] + 1))
                continue
            end
            new_collected = sort(vcat(pos[3], found_key))
            push!(Q, (py, px, new_collected, pos[4] + 1))

        elseif is_door(py, px)
            if lowercase(grid[py][px]) in pos[3]
                push!(Q, (py, px, pos[3], pos[4] + 1))
            end
        end
    end
end
