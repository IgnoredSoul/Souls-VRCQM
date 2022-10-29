# Item Functions | Old UI

<details>
<summary>Bools And Shit</summary>
<br>

```
[bool] ItemOrbit
[bool] ItemHider
[bool] ButterFingers
[bool] SelButterFingers
[bool] AntiTheft
[List<VRC_Pickup>] cachedList
[GameObject] orbObj;
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
<summary>Butter Fingers</summary>
<br>

```
Butter Fingers:
Loops through item cache and checks if your not the owner of said object, become its owner.
```
</details>
<br/>
<details>
<summary>Force Grab</summary>
<br>

```
Force Grab:
Loops through item cache again... then applies these

AutoHold = VRC_Pickup.AutoHoldMode.Yes;
allowManipulationWhenEquipped = true;
DisallowTheft = false;
MomentumTransferMethod = ForceMode.Force;
proximity = 999;
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
I used world clients item orbit as a base and modified it
to check for shit.. so really credit goes to them!

I really cant be fucked explaining it so heres the code

orbObj.transform.position = player.transform.position + new Vector3(0f, 0.2f, 0f);
orbObj.transform.Rotate(new Vector3(0f, 0.2f * Time.deltaTime, 0f));
for (int i = 0; i < cachedList.Count; i++)
{
    Extensions.CheckForOwnerShipPickups(cachedList[i]);
    cachedList[i].transform.position = orbObj.transform.position + orbObj.transform.forward * 1f;
    orbObj.transform.Rotate(new Vector3(0f, (360 / cachedList.Count), 0f));
}
```
</details>
