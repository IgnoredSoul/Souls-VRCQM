# Note!
I wont be adding item crashing and shit like that, player head swarm and item orbit is as far as I will go. 

If you want propper force pickups. Get [Astral Pickups]("https://github.com/Astrum-Project/AstralPickups/blob/master/Orbit.cs")!

# Item Functions | Release

<details>
<summary>Bools And Shit</summary>
<br>

```
[bool] Item Orbit
- [float] Orbit Speed
- [float] Orbit Height
- [float] Orbit Radius

[bool] Item Hider

[bool] Butter Fingers
[bool] Select Butter Fingers

[bool] Anti Theft

[bool] Player Head Swarm
```
</details>
<br/>
<details>
<summary>Item Caching And Clearing</summary>
<br>

```
ClearCache:
Literally just cachedList.Clear();

CachePickups:
Gets every active item and caches it.
```
</details>
<br/>
<details>
<summary>Loop Interval Slider</summary>
<br>

```
Loop Interval:
How slow does one loop take (seconds). Min: 0 Max: 2
```
</details>
<br/>
<details>
<summary>Butter Fingers</summary>
<br>

```
Butter Fingers:
Loops through item cache and checks if your not the owner of said object, become its owner.
```
</details>
<br/>
<details>
<summary>Anti Theft</summary>
<br>

```
Anti Theft:
Does some funky checks.
Basically it checks for the item currently in hand.
If the item is no longer in your hand but your still "holding" the item.
It just comes back to your hand.

Thanks For The Help: WC \\ _1254
```
</details>
<br/>
<details>
<summary>Bring, Respawn And Toggle Pickups</summary>
<br>

```
Once again. Get cache of items..

Bring Pickups:
Gets the object's pos and sets its pos to your pos.

Respawn Pickups:
Sends object's to 1000, 1000, 1000 so they respawn.

Show / Hide Pickups:
Gets object's gameObject and toggles it between true and false.
```
</details>
<br/>
<details>
<summary>Item Orbit</summary>
<br>

```
Item Orbit:
I used astral pickups item orbit as a base and modified it.
I fucking re-learnt trig to modify it.. It was that hard surprisingly.
```
</details>
<br/>
<details>
<summary>Orbit Sliders</summary>
<br>

```
Speed:
How fast it circles the player. Min: 0 Max: 5

Height:
At 0 the height is at their hips. Min: -10 Max: 10

Radius:
Distance between the player, also spreads the items. Min: 0 Max: 2.5
```
</details>
<br/>
<details>
<summary>Player Head Swarm</summary>
<br>

```
Player Head Swarm:
Sets the items position to the players head... Thats it
```
</details>

<br/>
