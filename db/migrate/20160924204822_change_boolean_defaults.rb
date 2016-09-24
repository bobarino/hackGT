class ChangeBooleanDefaults < ActiveRecord::Migration
  def change
    change_column :purchases, :paid, :boolean, :default => false
    change_column :purchases, :ext, :boolean, :default => false
    change_column :payouts, :paid, :boolean, :default => false
    add_column :purchases, :purchase_id, :string
    add_column :payouts, :purchase_id, :string
  end
end
