from django.contrib import admin

from products.models import (BedLinen, Bedspread, Blanket, KitchenTextile,
                             MattressCovers, Pillow, Pillowcase, Plaid,
                             Product, Sheet, Tablecloths, Towel)


class BlanketAdminInline(admin.TabularInline):
    model = Blanket


class TowelAdminInline(admin.TabularInline):
    model = Towel


class BedLinenAdminInline(admin.TabularInline):
    model = BedLinen


class PillowAdminInline(admin.TabularInline):
    model = Pillow


class PlaidAdminInline(admin.TabularInline):
    model = Plaid


class BedspreadAdminInline(admin.TabularInline):
    model = Bedspread


class MattressCoversAdminInline(admin.TabularInline):
    model = MattressCovers


class TableclothsAdminInline(admin.TabularInline):
    model = Tablecloths


class PillowcaseAdminInline(admin.TabularInline):
    model = Pillowcase


class KitchenTextileAdminInline(admin.TabularInline):
    model = KitchenTextile


class SheetAdminInline(admin.TabularInline):
    model = Sheet


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()

        dict_category = {
            0: TowelAdminInline(self.model, self.admin_site),
            1: BlanketAdminInline(self.model, self.admin_site),
            2: BedLinenAdminInline(self.model, self.admin_site),
            3: PillowAdminInline(self.model, self.admin_site),
            4: PlaidAdminInline(self.model, self.admin_site),
            5: BedspreadAdminInline(self.model, self.admin_site),
            6: MattressCoversAdminInline(self.model, self.admin_site),
            7: TableclothsAdminInline(self.model, self.admin_site),
            8: PillowcaseAdminInline(self.model, self.admin_site),
            9: KitchenTextileAdminInline(self.model, self.admin_site),
            10: SheetAdminInline(self.model, self.admin_site),
        }

        if obj.category is not None:
            return [dict_category[obj.category]]
        return list()
