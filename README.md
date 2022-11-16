# wizset

cli for WiZ smart bulbs

```
wizset <command>

COMMANDS
    scan                        -- scans for bulbs
    rgb <r> <g> <b> [<B>]       -- set rgb for all bulbs
    scene <scene_number>        -- set scene for all bulbs
    off                         -- turn all bulbs off
    group <group_subcmd>        -- group related, see GROUP section
    bulb <bulb_subcmd>          -- bulb related, see BULB section


BULB_SUBCOMMANDS
    list                        -- list bulbs
    <bulb_idx> <action>         -- single bulb control
    ACTIONS
        rgb <r> <g> <b> [<B>]   -- set rgb for bulb
        scene <scene_number>    -- set scene for bulb
        off                     -- turn bulb off
        flash                   -- bulb go flash
        alias <name>            -- set alias


GROUP_SUBCOMMANDS
    list                        -- list groups
    create <group_name>         -- create new group
    delete <group_name>         -- delete group
    <group_name> <action>       -- group specific
    ACTIONS
        bulbs                   -- list bulbs in group
        toggle [<bulb_idx>]     -- add or remove bulb from group
        rgb <r> <g> <b> [<B>]   -- set rgb for bulbs in group
        scene [<scene_number>]  -- set scene for bulbs in group
        off                     -- turn bulbs in group off
```
