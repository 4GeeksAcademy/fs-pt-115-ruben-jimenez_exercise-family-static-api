"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    # This method generates a unique incremental ID //Este método genera un ID único e incremental.
    def _generate_id(self):
        id_ = self._next_id
        self._next_id += 1
        return id_

    def add_member(self, member):
        ## You have to implement this method// Tienes que implementar este método.
        ## Append the member to the list of _members // Añadir el miembro a la lista _members.
        new_id = self._generate_id()
        member_to_add = {
            "id": new_id,
            "first_name": member["first_name"],
            "last_name": self.last_name,
            "age": member["age"],
            "lucky_numbers": member["lucky_numbers"],
        }
        self._members.append(member_to_add)
        return member_to_add

    def delete_member(self, id):
        ## You have to implement this method// Tienes que implementar este método.
        ## Loop the list and delete the member with the given id //Recorre la lista y elimina el miembro con el id dado.
        for i, m in enumerate(self._members):
            if m["id"] == id:
                del self._members[i]
                return True
        return False

    def get_member(self, id):
        ## You have to implement this method// Tienes que implementar este método.
        ## Loop all the members and return the one with the given id //Recorre todos los miembros y devuelve aquel cuyo id coincida con el proporcionado.
        for m in self._members:
            if m["id"] == id:
                return m
        return None
    # This method is done, it returns a list with all the family members// Este método está listo; devuelve una lista con todos los miembros de la familia. 
    def get_all_members(self):
        return self._members