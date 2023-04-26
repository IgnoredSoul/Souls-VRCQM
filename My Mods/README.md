# Note!
I wont be adding item crashing and shit like that, player head swarm and item orbit is as far as I will go. 

If you want propper force pickups. Get [Astral Pickups]("https://github.com/Astrum-Project/AstralPickups/blob/master/Orbit.cs")!

# Item Manipulator | Release 4.1.0

<details>
<summary>Variables</summary>
<br>

```
[List<VRC_Pickups>] cachedList
[List<VRC_Pickups>] cachedActiveList
[float] UpdateInterval

Item Orbit:
- [bool] Item Orbit Toggle
- [float] Orbit Speed
- [float] Orbit Height
- [float] Orbit Radius

Item Hider:
- [bool] Item Hider

Butter Fingers:
- [bool] Butter Fingers Toggle
- [bool] Select Butter Fingers Toggle

Anti Thieft:
- [bool] Anti Theft Toggle

Head Swarm:
- [bool] Head Swarm Toggle

Flies:
- [bool] Flies Toggle
```
</details>
<br/>

<details>
<summary>Scripts</summary>
<br>

```
ClearCache:
Literally just cachedList.Clear();
```

```
CachePickups:
Get's every active item and caches it.
```

```
Loop Interval:
How slow does one loop take (seconds). Min: 0 Max: 2
```

```
Butter Fingers:
Loops through the item cache and checks if your not the owner of said object. If not, become its owner.
```

```
Anti Theft:
Does some funky checks.
Basically it checks for the item currently in hand.
If the item is no longer in your hand but your still "holding" the item.
It just comes back to your hand.

Thanks For The Help: WC \\ _1254
```

```
Bring Pickups:
Loops throught the item cache. get's the object's pos and sets its pos to your pos.
```

```
Respawn Pickups:
Loops throught the item cache and sends object's to 1000, 1000, 1000 so they respawn.
```

```
Show / Hide Pickups:
Loops throught the item cache and checks for items that are active. Create a temp list and put them there. Then loop through that cache and get's the object's gameObject and toggles it between true and false.
```

```
Item Orbit:
I used astral pickups item orbit as a base and modified it for quest since quest is shit.
I fucking re-learnt trig to modify it.. It was that hard surprisingly.

Speed:
How fast it circles the player. Min: 0 Max: 5

Height:
At 0 the height is at their hips. Min: -10 Max: 10

Radius:
Distance between the player, also spreads the items. Min: 0 Max: 2.5
```

```
Player Head Swarm:
Sets the items position to the players head... Thats it
```

```
Flies:
Loops through the item cache and sets its position to the player with a random offset. (-5, 5)
```
</details>

<br/>

# Prime Gaming | Release 2.0.0

<details>
<summary>Variables</summary>
<br>

```
W.I.P
```

</details>

<br/>

<details>
<summary>Scripts</summary>
<br>

```
W.I.P
```

</details>
